from unittest import TestCase
from DailyTransportation import algorithm
from unittest import mock
import random


class Test(TestCase):

    # zero case test
    def test__calculate_euclidean_dist(self):
        result = algorithm._calculate_euclidean_dist((0.0, 0.0), (0.0, 0.0))
        self.assertEqual(result, 0)
    #test negative case with expected random=1
    def test__calculate_euclidean_dist(self):
        result = algorithm._calculate_euclidean_dist((-1.0, 0.0), (-2.0, 0.0))
        self.assertEqual(result, 1.0)
