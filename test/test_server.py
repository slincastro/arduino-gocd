import unittest

from src.server import Server


class TestArm(unittest.TestCase):
    def test_should_return_server_url(self):
        server = Server("http", "localhost", "EjercicioTDD")

        self.assertEquals(server.url, "http://localhost/go/api/pipelines/EjercicioTDD/status")
