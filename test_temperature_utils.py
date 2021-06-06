from temperature_utils import convert_temperature
import unittest

class TestTemperatureConversion(unittest.TestCase):

    def test_invalid(self):
        """
        There's no such temperature as -280 C, so convert_temperature should
        raise a ValueError.
        """
        self.assertRaises(ValueError, convert_temperature, -280, 'C', 'F')

    def test_valid(self):
        """ A series of valid temperature conversions to test. """

        test_cases = [((273.16, 'K',), (0.01, 'C')),
                      ((-40, 'C'), (-40, 'F')),
                      ((450, 'F'), (505.3722222222222, 'K'))]

        for test_case in test_cases:
            ((from_val, from_unit), (to_val, to_unit)) = test_case
            result = convert_temperature(from_val, from_unit, to_unit)
            self.assertAlmostEqual(to_val, result)

    def test_no_conversion(self):
        """
        Ensure that if the from-units and to-units are the same the
        temperature is returned exactly as it was passed and not converted
        to and from Kelvin, which may cause loss of precision.

        """
        T = 56.67
        result = convert_temperature(T, 'C', 'C')
        self.assertEqual(result, T)

    def test_bad_units(self):
        """ Check that ValueError is raised if invalid units are passed. """
        self.assertRaises(ValueError, convert_temperature, 0, 'C', 'R')
        self.assertRaises(ValueError, convert_temperature, 0, 'N', 'K')
