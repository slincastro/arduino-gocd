import json


class Pipeline:
    def __init__(self):
        self.instance = None

    def get_instance(self, instance_response):
        json_object = json.loads(instance_response)
        self.instance = json_object["pagination"]["total"]
        return str(self.instance)

    def get_status(self, status_response):
        json_object = json.loads(status_response)
        stages = json_object["stages"]
        final_stage = stages[len(stages) - 1]
        return final_stage["result"]
