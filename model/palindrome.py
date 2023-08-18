from datetime import datetime
from car import Car
from engines.sternman import SternmanEngine
from batteries.spindler import SpindlerBattery

class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        palindrome_engine = SternmanEngine(warning_light_is_on)
        palindrome_battery = SpindlerBattery(last_service_date)


        super().__init__(palindrome_battery, palindrome_engine)

        self.engine = palindrome_engine
        self.battery = palindrome_battery
        
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
