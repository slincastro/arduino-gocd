import json


class Pipeline:
    def __init__(self, response):
        self.instance = None
        self._response = response

    @property
    def get_instance(self):
        json_object = json.loads(self._response)
        self.instance = json_object["pagination"]["total"]
        return self.instance

    def get_status(self, status_response):
        json_object = json.loads(status_response)
        stages = json_object["stages"]
        final_stage = stages[len(stages)-1]
        return final_stage["result"]
