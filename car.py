from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_on):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.current_mileage = current_mileage
        self.last_service_date = last_service_date
        self.last_service_mileage = last_service_mileage
        self.warning_light_on = warning_light_on

    @abstractmethod
    def needs_service(self):
        pass


class CarFactory:
    def __init__(self) -> None:
        pass

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(current_date, last_service_date, warning_light_on)

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(current_date, last_service_date, current_mileage, last_service_mileage)
