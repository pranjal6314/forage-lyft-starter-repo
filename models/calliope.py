from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.spindler_battery import SpindlerBattery
from tires.octoprime_tire import OctoprimeTire

class Calliope(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, tire_sensor_data): # tire_sensor_data is a list of tire pressure values
        calliope_engine = CapuletEngine(current_mileage, last_service_mileage)
        calliope_battery = SpindlerBattery(last_service_date)
        calliope_tire = OctoprimeTire(tire_sensor_data) # this is a list of tire pressure values

        super().__init__(calliope_engine, calliope_battery, calliope_tire)

        self.engine = calliope_engine
        self.battery = calliope_battery
        self.tire = calliope_tire # this is a list of tires 
    
    def needs_service(self):
        return super().needs_service()
