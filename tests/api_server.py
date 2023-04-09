import os
from pathlib import Path
from node_chatgpt_api import BingAIClient, BingMessage, start_api_server

start_api_server(os.path.join(Path(os.getcwd()).parent.absolute(), "settings.js"))

client = BingAIClient()
response = client.ask(BingMessage("How are you?"))

print(response.error)
print(response.response)
