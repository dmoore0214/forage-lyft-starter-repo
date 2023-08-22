from datetime import datetime
from car import Car
from engine.engines.willoughby import WilloughbyEngine
from engine.batteries.spindler import SpindlerBattery
from engine.tires.carrigan import CarriganTire

class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, tire_sensor_data):
        glissade_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        glissade_battery = SpindlerBattery(last_service_date)
        glissade_tire = CarriganTire(tire_sensor_data)
    
        super().__init__(glissade_battery, glissade_engine, glissade_tire)
        self.engine = glissade_engine
        self.battery = glissade_battery
        self.tire = glissade_tire
        
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
