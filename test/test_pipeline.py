import os
import unittest

from src.pipeline import Pipeline


class TestPipeline(unittest.TestCase):
    def test_should_be_return_number_intances(self):
        instances = '7'

        response = '{ "pagination": { "offset": 100000000, "total": 7, "page_size": 10 }, "pipelines": []}'

        pipeline = Pipeline()

        self.assertEquals(pipeline.get_instance(response), instances)

    def test_should_be_return_pipeline_status_failed(self):
        path = os.getcwd()
        response_fine_name = 'instance_pipeline.json'
        response_file = path + '/test/resources/' + response_fine_name

        response = open(response_file, 'r').read()

        pipeline = Pipeline()

        self.assertEquals(pipeline.get_status(response), 'Failed')

    def test_should_be_return_pipeline_status_Passed(self):
        path = os.getcwd()
        response_fine_name = 'instance_pipeline_passed.json'
        response_file = path + '/test/resources/' + response_fine_name

        response = open(response_file, 'r').read()

        pipeline = Pipeline()

        self.assertEquals(pipeline.get_status(response), 'Passed')
