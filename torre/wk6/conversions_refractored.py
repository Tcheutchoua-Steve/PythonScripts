
class UnitsNotExisting(Exception): pass

def convert(fromUnit, toUnit, value) :
    #meter  = kelvin = celcius = fahrenheit = miles = yards = False

    temperature = ['celcius', 'fahrenheit','kelvin']
    distance = ['meter','yard','miles']
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    if (fromUnit != toUnit and (fromUnit in temperature) and toUnit in temperature) :
        if fromUnit == "celcius" :
            if toUnit == "kelvin" :
                return value + 273.15
            elif toUnit == "fahrenheit" :
                return  value * (9/5) + 32
        elif fromUnit =="kelvin" :
            if toUnit == "celcius" :
                return value - 273.15
            elif toUnit == "fahrenheit" :
                return  value * (9/5) - 459.67
        elif fromUnit == "fahrenheit" :
            if toUnit =="celcius" :
                return (value - 32) * (5/9)
            elif toUnit =="kelvin" :
                return  (value + 459.67) * (5/9)


        else:
            raise UnitsNotExisting("The units you entered are not existing")

    if (fromUnit != toUnit and (fromUnit in distance) and (toUnit in distance)) :
        if fromUnit == "meter" :
            if toUnit == "miles":
                return value * 0.000621371
            elif toUnit == "yard" :
                return value * 1.09361
        elif fromUnit == "miles" :
            if toUnit == "meter" :
                return value * 1609.34
            elif toUnit == "yard" :
                return value * 1760
        elif fromUnit == "yard" :
            if toUnit == "meter" :
                return value * 0.9144
            elif toUnit == "mile" :
                return value *  (1/1760)
        else :
            raise UnitsNotExisting("The units you entered are not existing")

