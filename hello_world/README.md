# Brainbase Runner Usage Guide

This guide will walk you through setting up and using the provided files to create a Brainbase worker and flow, and to start a chat session via a WebSocket. An alternative web client option is also provided.

## Prerequisites

- Python 3.7 or later
- pip (Python package installer)
- Basic command-line knowledge

## Initial Setup

1.  **Clone or Download the Repository**

    Ensure you have the following key files in your project:

    - hello_world/brainbase_chat.py
    - hello_world/demo.py
    - hello_world/setup.py
    - hello_world/.env.example

2.  **Create a Virtual Environment (Optional but Recommended)**

    Run the following commands:

        python -m venv venv
        source venv/bin/activate   # On Windows, use: venv\Scripts\activate

3.  **Install Required Pip Packages**

    Install the necessary packages with pip:

        pip install -r requirements.txt

4.  **Configure Environment Variables**

    In the `hello_world` directory, create a file named `.env` using the provided `.env.example` as a template. At a minimum, include your Brainbase API key. For example:

        BRAINBASE_API_KEY=your_brainbase_api_key

## Creating a Worker and Flow

The `setup.py` script will create a new worker and a flow in Brainbase. It performs the following actions:

- Loads environment variables from the `.env` file.
- Creates a BrainbaseLabs client.
- Creates a new worker (named "Hello World Worker").
- Creates a new flow version for that worker.

You can also modify the original source code in the `.based` file to customize the worker's behavior.

To run the script, execute the following command from the `hello_world` directory:

    python setup.py

After executing, the script will print out the new worker ID and flow ID. Save these IDs for the chat session.

## Using demo.py to Chat via WebSocket

The `demo.py` script uses the `BrainbaseRunner` class to connect to the Brainbase engine via a WebSocket and start a chat session. It requires the worker ID and flow ID generated from `setup.py`.

Usage:

    python demo.py <worker_id> <flow_id>

Replace `<worker_id>` and `<flow_id>` with the IDs you obtained. For example:

    python demo.py worker_123 flow_456

Once connected, your terminal will prompt with "You:" where you can enter your messages. Type "exit" or "quit" to close the chat session.

## Alternative: Using the Brainbase Web Client

If you prefer a graphical interface, you can use the Brainbase Web Client available at [https://brainbase-ws-client.vercel.app/](https://brainbase-ws-client.vercel.app/).

Steps:

1. Open your browser and navigate to the above URL.
2. Enter the following details into the web client:
   - **API Key:** Your Brainbase API key (from your `.env` file)
   - **Worker ID:** The worker ID from `setup.py`
   - **Flow ID:** The flow ID from `setup.py`
3. Connect to start chatting using the web interface.

## Summary

- **Setup:** Configure your environment and install dependencies.
- **Worker & Flow Creation:** Run `setup.py` to generate your worker and flow IDs.
- **Chat Session:** Use `demo.py` with your IDs to initiate a WebSocket chat session.
- **Web Client Alternative:** Use the [Brainbase Web Client](https://brainbase-ws-client.vercel.app/) for a browser-based chat experience.

Enjoy interacting with Brainbase!
