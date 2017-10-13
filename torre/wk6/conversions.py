
class TypeError(Exception): pass

############################################     Celcius Conversions         ###################################################

def convertCelciusToKelvins(celcius) :

    if isinstance(celcius,float) :
    #return 0.0
        return celcius + 273.15
    else :
        raise TypeError(" Please enter float input")

def convertCelciusToFahrenheit(celcius) :
    if isinstance(celcius,float) :
    #return  0.0
        return  celcius * (9/5) + 32
    else :
        raise TypeError("Please enter float input")

############################################     Fahrenheit Conversions         ###################################################

def convertFahrenheitToCelcius(fah) :

    if isinstance(fah,float) :
    #return 0.0
        return (fah - 32) * (5/9)
    else :
        raise TypeError(" Please enter float input")

def convertFahrenheitToKevins(fah) :
    if isinstance(fah,float) :
    #return  0.0
        return  (fah + 459.67) * (5/9)
    else :
        raise TypeError("Please enter float input")

############################################     Kevin Conversions         ###################################################
def convertKelvinToCelcius(kelvin) :

    if isinstance(kelvin,float) :
    #return 0.0
        return kelvin - 273.15
    else :
        raise TypeError(" Please enter float input")

def convertKelvinToFahrenheit(kelvin) :
    if isinstance(kelvin,float) :
    #return  0.0
        return  kelvin * (9/5) - 459.67
    else :
        raise TypeError("Please enter float input")




