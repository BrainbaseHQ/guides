import asyncio
import json
import aiohttp

class BrainbaseRunner:
    def __init__(self, worker_id, flow_id, api_key, host="wss://brainbase-engine-python.onrender.com"):
        self.worker_id = worker_id
        self.flow_id = flow_id
        self.api_key = api_key
        self.host = host
        # Construct the URL using a secure WebSocket connection.
        self.url = f"{self.host}/{self.worker_id}/{self.flow_id}?api_key={self.api_key}"
    
    async def start(self):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect(self.url) as ws:
                print(f"Connected to {self.url}")
                # Send an initialization message to the engine.
                await self._initialize(ws)
                # Create tasks: one to listen to server messages and one to let the user send chat messages.
                listen_task = asyncio.create_task(self._listen(ws))
                chat_task = asyncio.create_task(self._chat(ws))
                # Wait until one of the tasks completes (e.g. the user exits, or the connection stops).
                done, pending = await asyncio.wait(
                    [listen_task, chat_task],
                    return_when=asyncio.FIRST_COMPLETED
                )
                # Cancel any remaining tasks.
                for task in pending:
                    task.cancel()
    
    async def _initialize(self, ws):
        init_data = {
            "streaming": True,
            "deploymentType": "development"
        }
        init_message = {
            "action": "initialize",
            "data": json.dumps(init_data)
        }
        await ws.send_str(json.dumps(init_message))
        print("Initialization message sent.")
    
    async def _listen(self, ws):
        try:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    try:
                        message_obj = json.loads(msg.data)
                        action = message_obj.get("action")
                        if action in ["message", "response"]:
                            print("Received message:", message_obj["data"].get("message"))
                        elif action == "stream":
                            print("Received stream chunk:", message_obj["data"].get("message"))
                        elif action == "function_call":
                            print("Function call requested:", message_obj["data"].get("function"))
                        elif action == "error":
                            print("Error from server:", message_obj["data"].get("message"))
                        elif action == "done":
                            print("Operation completed successfully:", message_obj["data"])
                        else:
                            print("Unknown action received:", action)
                    except Exception as e:
                        print("Error parsing message:", e)
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    print("WebSocket error:", ws.exception())
                    break
        except Exception as e:
            print("Listener task encountered an error:", e)
    
    async def _chat(self, ws):
        loop = asyncio.get_event_loop()
        # Loop to get user input and then send it via the WebSocket.
        while True:
            # Use run_in_executor to avoid blocking the event loop.
            user_input = await loop.run_in_executor(None, input, "You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat...")
                await ws.close()
                break
            chat_message = {
                "action": "message",
                "data": {"message": user_input}
            }
            try:
                await ws.send_str(json.dumps(chat_message))
            except Exception as e:
                print("Failed to send message:", e)
                break
