class Server(object):
    def __init__(self, protocol, host, pipeline):
        self._protocol = protocol
        self._host = host
        self._pipeline = pipeline

    @property
    def history_url(self):
        return self._protocol + "://" + self._host + "/go/api/pipelines/" + self._pipeline + "/history/100000000"

    @property
    def pipeline_url(self):
        return self._protocol + "://" + self._host + "/go/api/pipelines/" + self._pipeline + "/instance/"
