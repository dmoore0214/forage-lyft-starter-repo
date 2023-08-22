from tires import Tires

class OctoprimeTire(Tires):
    def __init__(self, tire_sensor_data):
        super().__init__(tire_sensor_data)
        self.tire_sensor_data = tire_sensor_data

    def tire_needs_service(self):
        return sum(self.tire_sensor_data) >= 3.0