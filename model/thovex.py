from datetime import datetime
from engines.capulet import CapuletEngine
from batteries.nubbin import NubbinBattery
from car import Car


class Thovex(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        thovex_engine = CapuletEngine(current_mileage, last_service_mileage)
        thovex_battery = NubbinBattery(last_service_date)

        super().__init__(thovex_engine, thovex_battery)
        self.engine = thovex_engine
        self.battery = thovex_battery
        
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
