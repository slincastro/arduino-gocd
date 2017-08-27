import time

import json
import requests

from src.arduino_client import Arduino

while True:
    host = 'http://localhost/go/api'
    pipeline_name = 'EjercicioTDD'
    request = requests.get(host + '/pipelines/' + pipeline_name + '/status')
    print request.content
    response = json.loads(request.content)

    print response['locked']
    print response['paused']
    print response['schedulable']

    locked = bool(response['locked'])
    paused = bool(response['paused'])
    schedulable = bool(response['schedulable'])

    arduino = Arduino()

    if not locked and not paused and not schedulable:
        arduino.send('b')
    else:
        arduino.send('a')

    time.sleep(5)
