import sys
import asyncio
import os
from brainbase_runner import BrainbaseRunner

async def main():
    if len(sys.argv) < 3:
        print("Usage: python demo.py <worker_id> <flow_id>")
        sys.exit(1)
    
    worker_id = sys.argv[1]
    flow_id = sys.argv[2]
    
    api_key = os.environ["BRAINBASE_API_KEY"]   # set your API key in .env

    connection = BrainbaseRunner(worker_id, flow_id, api_key)
    await connection.start()

if __name__ == '__main__':
    asyncio.run(main())
