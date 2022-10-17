from battery.nubbin_battery import NubbinBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tyre):
        self.engine = engine
        self.battery = battery
        self.tyre = tyre

    def needs_service(self):
        engine_service = self.engine.needs_service()
        battery_service = self.battery.needs_service()
        tyre_service = self.tyre.needs_service()
        # could use a conditional statement to display which one needs service

        return engine_service or battery_service or tyre_service


class CarFactory:
    def __init__(self) -> None:
        pass

    def create_calliope(last_service_date, current_mileage, last_service_mileage, sensor_array):
        return Car(engine=CapuletEngine(current_mileage, last_service_mileage), battery=SpindlerBattery(last_service_date))

    def create_glissade(last_service_date, current_mileage, last_service_mileage, sensor_array):
        return Car(engine=WilloughbyEngine(current_mileage, last_service_mileage), battery=SpindlerBattery(last_service_date))

    def create_palindrome(last_service_date, warning_light_is_on, sensor_array):
        return Car(engine=SternmanEngine(warning_light_is_on), battery=SpindlerBattery(last_service_date))

    def create_rorschach(last_service_date, current_mileage, last_service_mileage,  sensor_array):
        return Car(engine=WilloughbyEngine(current_mileage, last_service_mileage), battery=NubbinBattery(last_service_date))

    def create_thovex(last_service_date, current_mileage, last_service_mileage, sensor_array):
        return Car(engine=CapuletEngine(current_mileage, last_service_mileage), battery=NubbinBattery(last_service_date))
