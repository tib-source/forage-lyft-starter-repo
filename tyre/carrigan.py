from re import L
from .tyre import Tyre


class Carrigan(Tyre):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        service = [x for x in self.sensor_array if x >= 0.9]
        if len(service) != 0:
            return True
        return False
