from unittest import TestCase
from DailyTransportation import clCar
from unittest.mock import Mock

json = Mock()
json.loads('{"ID": "151651"}', '{"car_type": "MAZDA"}', '{"driver_cost": "15611"}', '{"cost_per_minute": 5}', '{"capacity": 10}', '{"wheelchair": "YES"}')

class TestCar(TestCase):
    def test_calculate_cost_time(self):
        res = clCar.Car.calculate_cost(json,5)
        self.assertEqual(res, 1515)
