import time
import json
import requests
import sys

from src.pipeline import Pipeline

sys.path.append('../')

from src.arduino_client import Arduino
from src.server import Server

while True:
    protocol = 'http'
    host = 'localhost'
    pipeline = 'x'
    gocd = Server(protocol, host, pipeline)

    instance_request = requests.get(gocd.history_url)

    pipeline = Pipeline(instance_request.content)

    state_request = requests.get(gocd.pipeline_url+pipeline.get_instance)

    print response['locked']
    print response['paused']
    print response['schedulable']

    locked = bool(response['locked'])
    paused = bool(response['paused'])
    schedulable = bool(response['schedulable'])

    # arduino = Arduino()

    # if not locked and not paused and not schedulable:
    #   arduino.send('b')
    # else:
    #   arduino.send('a')

    time.sleep(5)
