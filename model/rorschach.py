from datetime import datetime
from car import Car
from engines.willoughby import WilloughbyEngine
from batteries.nubbin import NubbinBattery

class Rorschach(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        rorschach_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        rorschach_battery = NubbinBattery(last_service_date)
        super().__init__(rorschach_engine, rorschach_battery)

        self.engine = rorschach_engine
        self.battery = rorschach_battery


    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
