from datetime import datetime
from car import Car
from engine.engines.capulet import CapuletEngine
from engine.batteries.spindler import SpindlerBattery
from engine.tires.octoprime import OctoprimeTire

class Calliope(Car):
    def __init__ (self, last_service_date, last_service_mileage, current_mileage,tire_sensor_data):
        calliope_battery = SpindlerBattery(last_service_date)
        calliope_engine = CapuletEngine(last_service_mileage, current_mileage)
        calliope_tire = OctoprimeTire(tire_sensor_data)

        super().__init__(calliope_engine, calliope_battery, calliope_tire)
        self.engine = calliope_engine
        self.battery = calliope_battery
        self.tire = calliope_tire
        
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
