class Response:
    error: str | None
    status: bool

    response: str | None
    conversationId: str | None
    messageId: str | None
    conversationSignature: str | None
    clientId: str | None
    invocationId: str | None
    details: str | None

    def __init__(self, raw_response):
        self.error = raw_response["error"]
        self.status = bool(self.error)

        if not self.status:
            return

        self.response = raw_response["response"]
        self.conversationId = raw_response["conversationId"]
        self.messageId = raw_response["messageId"]
        self.conversationSignature = raw_response["conversationSignature"]
        self.clientId = raw_response["clientId"]
        self.invocationId = raw_response["invocationId"]
        self.details = raw_response["details"]


class BingResponse(Response):
    jailbreakConversationId: str | bool | None

    def __init__(self, raw_response):
        super().__init__(raw_response)
        self.jailbreakConversationId = raw_response["jailbreakConversationId"]
