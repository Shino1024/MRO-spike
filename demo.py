from abc import abstractmethod, ABC

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import os
import sys
import time


class MCVModelUsage(ABC):
    def __init__(self, endpoint_url, subscription_key, feature):
        self._endpoint_url = endpoint_url
        self._subscription_key = subscription_key
        self._feature = feature
        self._final_output = None

    def run_analyze(self):
        pass

    def get_final_output(self):
        return self._final_output

    @abstractmethod
    def do_work(self):
        pass


class MCVModelUsageConcreteImpl(MCVModelUsage):
    pass


class MCVImageDescriptor(MCVModelUsage):
    pass


cv_model_usages = [
    #
]

if __name__ == "__main__":
    endpoint = "https://mcvdemo.cognitiveservices.azure.com/"
    with open(".apipass", "r") as apiPassFile:
        subscription_key = apiPassFile.readline()


