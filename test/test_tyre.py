import unittest
from tyre.carrigan import Carrigan
from tyre.octoprime import Octoprime


class TestCarrigan(unittest.TestCase):
    def test_should_be_serviced(self):
        sensor_array = [0, 1, 0.2, 0.5]
        tyre = Carrigan(sensor_array)

        self.assertTrue(tyre.needs_service())

    def test_should_not_be_serviced(self):
        sensor_array = [0.1, 0.2, 0.13, 0.23]
        tyre = Carrigan(sensor_array)

        self.assertFalse(tyre.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_should_be_serviced(self):
        sensor_array = [0.82, 1.3, 1.2, 0.5]
        tyre = Octoprime(sensor_array)

        self.assertTrue(tyre.needs_service())

    def test_should_not_be_serviced(self):
        sensor_array = [0.1, 0.2, 0.13, 0.23]
        tyre = Octoprime(sensor_array)

        self.assertFalse(tyre.needs_service())


if __name__ == "main":
    unittest.main()
