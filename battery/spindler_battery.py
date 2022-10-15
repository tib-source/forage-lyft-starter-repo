
from abc import ABC

from battery.battery import Battery


class SpindlerBattery(Battery, ABC):
    def __init__(self, current_date, last_service_date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date
        pass

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 4)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False
