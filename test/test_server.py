import unittest

from src.server import Server


class TestServer(unittest.TestCase):
    def test_should_return_history_url(self):
        server = Server("http", "localhost", "piarm")

        self.assertEquals(server.history_url, "http://localhost/go/api/pipelines/piarm/history/100000000")

    def test_should_return_pipelines_url(self):
        server = Server("http", "localhost", "piarm")

        self.assertEquals(server.pipeline_url, "http://localhost/go/api/pipelines/piarm/instance/")
