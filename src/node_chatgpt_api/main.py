import requests
import json
from .types.message import Message, BingMessage
from .types.response import Response, BingResponse
from .helpers.install import _start_api_server


def start_api_server(settings_path: str):
    """
    Starts the node-chatgpt-api server in a separate thread
    :param settings_path: the absolute path to the settings.js, find an example here: https://github.com/waylaidwanderer/node-chatgpt-api/blob/main/settings.example.js
    """

    return _start_api_server(settings_path)


class Client:
    def __init__(self, url="http://localhost:3000", **kwargs):
        self.url = url
        self.kwargs = kwargs

    def request(self, message: Message | BingMessage, **kwargs):
        data = message.to_dict()

        if kwargs:
            kwargs = self.kwargs.copy().update(kwargs)
            data = message.to_dict() | kwargs

        res = requests.post(self.url + "/conversation",
                            json=data).json()

        return res

    def ask(self, message: Message, **kwargs) -> Response:
        res = self.request(message, **kwargs)
        return Response(res)


class BingAIClient(Client):
    def __init__(self, url="http://localhost:3000", **kwargs):
        super().__init__(url, **kwargs)

        if self.kwargs.get("jailbreakConversationId"):
            self.kwargs.update(
                dict(jailbreakConversationId=self.ask(
                    BingMessage("Hi, who are you?", jailbreakConversationId=True)).jailbreakConversationId)
            )

    def ask(self, message: BingMessage, **kwargs) -> BingResponse:
        res = self.request(message, **kwargs)
        return BingResponse(res)
