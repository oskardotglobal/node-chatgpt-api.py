import requests
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

    def ask(self, message: Message, **kwargs) -> Response:
        kwargs.update(self.kwargs)

        json = requests.post(self.url + "/conversation",
                             data=message.to_dict().update(**kwargs)).json()

        return Response(json)


class BingAIClient(Client):
    def __init__(self, url="http://localhost:3000", **kwargs):
        super().__init__(url, **kwargs)

        if kwargs.get("jailbreakConversationId"):
            kwargs.update(
                dict(jailbreakConversationId=self.ask(
                    BingMessage("Hi, who are you?", jailbreakConversationId=True)).jailbreakConversationId)
            )

    def ask(self, message: BingMessage, **kwargs) -> BingResponse:
        kwargs.update(self.kwargs)

        json = requests.post(self.url + "/conversation",
                             data=message.to_dict().update(**kwargs)).json()

        return BingResponse(json)
