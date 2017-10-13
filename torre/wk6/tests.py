""" Unit tests for conversions.py"""

import conversions
import unittest
import conversions_refractored

############################################     Celcius Conversions         ###################################################

class SomeCelciusValuesToKelvins(unittest.TestCase) :
    def testFromCelciusToKelvinPositive(self):
        print("Checking if the conversion of 500.00 C is 773.15k")
        self.assertAlmostEqual(conversions.convertCelciusToKelvins(500.00) ,773.15, places=2)

    def testFromCelciusToKelvinNegative(self):
        print("Checking if the conversion of -140.00 C is 133.15k")
        self.assertAlmostEqual(133.15 , conversions.convertCelciusToKelvins(-140.00) , places=2)

    def testFromCelciusToKelvinZero(self):
        print("Checking if the conversion of 00.00 C is 273.15")
        self.assertAlmostEqual(273.15, conversions.convertCelciusToKelvins(0.00 ) , places=2)



class SomeCelciusValuesToFahrenheit (unittest.TestCase) :
    def testFromCelciusToFahrenheitZero(self):
        print("Checking if the conversion of 00.00 C is 32.00F")
        self.assertAlmostEqual( 32.00, conversions.convertCelciusToFahrenheit(0.00) , places=2)

    def testFromCelciusToFahrenheitPositive(self):
        print("Checking if the conversion of 500.00 C is 932.00F")
        self.assertAlmostEqual(932.00 , conversions.convertCelciusToFahrenheit(500.00) , places=2)


    def testFromCelciusToFahrenheitNegative(self):
        print("Checking if the conversion of -140.00 C is -220.00F")
        self.assertAlmostEqual(-220.00, conversions.convertCelciusToFahrenheit(-140.00) , places=2)

class CelciusToKelvinBadInput(unittest.TestCase) :
    """Test fails with integer given as input"""
    def testIntegerInput(self):
        print("Check if 0 produces type error ")
        self.assertRaises(conversions.TypeError,conversions.convertCelciusToKelvins, 0)

    def testStringInput(self):
        print("Check if aa produces type error ")
        self.assertRaises(conversions.TypeError,conversions.convertCelciusToKelvins, "aa")

class CelciusToFahrenheitBadInput(unittest.TestCase) :
    def testIntegerInput(self):
        print("Check if 0 produces type error ")
        self.assertRaises(conversions.TypeError,conversions.convertCelciusToFahrenheit, 0)

    def testStringInput(self):
        print("Check if aa produces type error")
        self.assertRaises(conversions.TypeError,conversions.convertCelciusToFahrenheit, "aa")

############################################     Fahrenheit Conversions         ###################################################

class SomeFahrenheitValuestoKelvins(unittest.TestCase) :
    def testFromFahrenheitToKelvinPositive(self):
        print("Checking if the conversion of 500.00F is 533.15k")
        self.assertAlmostEqual(533.15, conversions.convertFahrenheitToKevins(500.00) , places=2)

    def testFromFahrenheitToKelvinNegative(self):
        print("Checking if the conversion of --166.00 F is 163.15k")
        self.assertAlmostEqual(163.15 , conversions.convertFahrenheitToKevins(-166.00) , places=2)

class SomeFahrenheitValuestoCelcius(unittest.TestCase) :
    def testFromFahrenheitToCelciusPositive(self):
        print("Checking if the conversion of 932.00F is 500.15C")
        self.assertAlmostEqual(500.00, conversions.convertFahrenheitToCelcius(932.00) , places=2)

class FahrenheitToCelciusBadInput(unittest.TestCase) :
    def testIntegerInput(self):
        print("Check if 0 produces type error")
        self.assertRaises(conversions.TypeError,conversions.convertFahrenheitToCelcius, 0)

    def testStringInput(self):
        print("Check if aa produces type error")
        self.assertRaises(conversions.TypeError,conversions.convertFahrenheitToCelcius, "aa")

class FahrenheitToKelvinBadInput(unittest.TestCase) :
    def testIntegerInput(self):
        print("Check if 0 produces type error")
        self.assertRaises(conversions.TypeError,conversions.convertFahrenheitToKevins, 0)

    def testStringInput(self):
        print("Check if aa produces type error")
        self.assertRaises(conversions.TypeError,conversions.convertFahrenheitToKevins, "aa")
############################################     Kelvin Conversions         ###################################################

class SomeKelvinValuestoFahrenheit(unittest.TestCase) :
    def testFromKevintoFahrenheitPositive(self):
        print("Checks if 503.15k produces 446.00F")
        self.assertAlmostEqual(446.00, conversions.convertKelvinToFahrenheit(503.15) , places=2)

class SomeKelvinValuestoCelcius(unittest.TestCase) :
    def testFromKevintoFahrenheitPositive(self):
        print("Checks if 773.15k produces 500.00F")
        self.assertAlmostEqual(500.00, conversions.convertKelvinToCelcius(773.15) , places=2)

class KelvintoFahrenheitBadInput(unittest.TestCase) :
    def testIntegerInput(self):
        print("Check if 0 produces type error")
        self.assertRaises(conversions.TypeError,conversions.convertKelvinToFahrenheit, 0)

    def testStringInput(self):
        print("Check if aa produces type error")
        self.assertRaises(conversions.TypeError,conversions.convertKelvinToFahrenheit, "aa")

class KelvintoCelciusBadInput(unittest.TestCase) :
    def testIntegerInput(self):
        print("Check if 0 produces type error")
        self.assertRaises(conversions.TypeError,conversions.convertKelvinToCelcius, 0)

    def testStringInput(self):
        print("Check if aa produces type error")
        self.assertRaises(conversions.TypeError,conversions.convertKelvinToCelcius, "aa")


#******************************************************     Check if Temperature Conversions are working **************************************
class CelciusToKelvin (unittest.TestCase):
    def testFromCelciusToKelvin(self):
        print("Checking if Combined Convertion converts celcius to kelvin , 500 to 773.15")
        self.assertAlmostEqual(conversions_refractored.convert("celcius","kelvin",500.00) ,773.15, places=2)


class CelciusToFahrenheit(unittest.TestCase):
    def testFromCelciusToFahrenheit(self):
        print("Checking if Combined Convertion converts celcius to fahrenheit , 0.0 to 32")
        self.assertAlmostEqual(conversions_refractored.convert("celcius","fahrenheit",00.00) ,32, places=2)

if __name__ == '__main__':
    unittest.main()
