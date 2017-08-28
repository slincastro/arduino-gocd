import time
import requests
import sys

sys.path.append('../')

from src.pipeline import Pipeline
from src.arduino_client import Arduino
from src.server import Server

while True:
    protocol = 'http'
    host = 'localhost'
    pipeline = 'piarm'
    gocd = Server(protocol, host, pipeline)
    arduino = Arduino()

    instance_request = requests.get(gocd.history_url)

    pipeline = Pipeline()

    state_request = requests.get(gocd.pipeline_url + pipeline.get_instance(instance_request.content))

    pipeline_status = pipeline.get_status(state_request.content)

    print pipeline_status

    if pipeline_status == 'Passed':
        arduino.send('b')
    else:
        arduino.send('a')

    time.sleep(5)
