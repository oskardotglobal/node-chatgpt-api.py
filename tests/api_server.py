import os
from pathlib import Path
from node_chatgpt_api import BingAIClient, BingMessage, start_api_server, stop_api_server
from util import enable_http_logs

#start_api_server(os.path.join(Path(os.getcwd()).parent.absolute(), "settings.js"))

enable_http_logs()

client = BingAIClient(jailbreakConversationId=True)
response = client.ask(BingMessage("How are you?"))

print(response.error)
print(response.response)

#stop_api_server()
