from datetime import datetime
from engine.engines.capulet import CapuletEngine
from engine.batteries.nubbin import NubbinBattery
from engine.tires.carrigan import CarriganTire
from car import Car


class Thovex(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, tire_sensor_data):
        thovex_engine = CapuletEngine(current_mileage, last_service_mileage)
        thovex_battery = NubbinBattery(last_service_date)
        thovex_tire = CarriganTire(tire_sensor_data)

        super().__init__(thovex_engine, thovex_battery, thovex_tire)
        self.engine = thovex_engine
        self.battery = thovex_battery
        self.tire = thovex_tire
        
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
