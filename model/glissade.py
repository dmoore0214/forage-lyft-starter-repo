from datetime import datetime
from car import Car
from engines.willoughby import WilloughbyEngine
from batteries.spindler import SpindlerBattery

class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        glissade_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        glissade_battery = SpindlerBattery(last_service_date)
    
        super().__init__(glissade_battery, glissade_engine)
        self.engine = glissade_engine
        self.battery = glissade_battery
        
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
