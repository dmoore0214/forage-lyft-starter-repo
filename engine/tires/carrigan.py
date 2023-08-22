
from tires import Tires

class CarriganTire(Tires):
    def __init__(self, tire_sensor_data):
        super().__init__(tire_sensor_data)
        self.tire_sensor_data = tire_sensor_data

    def tire_needs_service(self):
        return any(map(lambda current_tire: current_tire >=0.9, self.tire_sensor_data))