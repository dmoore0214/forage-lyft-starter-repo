from datetime import datetime
from car import Car
from engines.capulet import CapuletEngine
from batteries.spindler import SpindlerBattery

class Calliope(Car):
    def __init__ (self, last_service_date, last_service_mileage, current_mileage):
        calliope_battery = SpindlerBattery(last_service_date)
        calliope_engine = CapuletEngine(last_service_mileage, current_mileage)

        super().__init__(calliope_engine, calliope_battery)
        self.engine = calliope_engine
        self.battery = calliope_battery
        
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
