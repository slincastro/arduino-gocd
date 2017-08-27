class Server(object):
    def __init__(self, protocol, server, pipeline):
        self._protocol = protocol
        self._server = server
        self._pipeline = pipeline

    @property
    def url(self):
        return self._protocol + "://" + self._server + "/go/api/pipelines/" + self._pipeline + "/status"
