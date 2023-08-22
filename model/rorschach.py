from datetime import datetime
from car import Car
from engine.engines.willoughby import WilloughbyEngine
from engine.batteries.nubbin import NubbinBattery
from engine.tires.octoprime import OctoprimeTire

class Rorschach(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, tire_sensor_data):
        rorschach_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        rorschach_battery = NubbinBattery(last_service_date)
        rorshach_tire = OctoprimeTire(tire_sensor_data)

        super().__init__(rorschach_engine, rorschach_battery,rorshach_tire)

        self.engine = rorschach_engine
        self.battery = rorschach_battery
        self.tire = rorshach_tire


    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
