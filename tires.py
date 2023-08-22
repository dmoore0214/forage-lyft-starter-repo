from abc import ABC, abstractmethod


class Tires(ABC):
    def __init__(self, tire_sensor_data):
        self.tire_sensor_date = tire_sensor_data
        

    @abstractmethod
    def tire_needs_service(self):
        pass