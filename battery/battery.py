from abc import ABC, abstractclassmethod


class Battery(ABC):
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def needs_service():
        pass
