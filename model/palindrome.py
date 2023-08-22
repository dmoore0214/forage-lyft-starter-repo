from datetime import datetime
from car import Car
from engine.engines.sternman import SternmanEngine
from engine.batteries.spindler import SpindlerBattery
from engine.tires.octoprime import OctoprimeTire

class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on, tire_sensor_data):
        palindrome_engine = SternmanEngine(warning_light_is_on)
        palindrome_battery = SpindlerBattery(last_service_date)
        palindrome_tire = OctoprimeTire(tire_sensor_data)


        super().__init__(palindrome_battery, palindrome_engine, palindrome_tire)

        self.engine = palindrome_engine
        self.battery = palindrome_battery
        self.tire = palindrome_tire
        
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
