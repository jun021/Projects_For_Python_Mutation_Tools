# temperature_utils.py

def convert_temperature(value, from_unit, to_unit):
    """ Convert and return the temperature value from from_unit to to_unit. """

    # Dictionary of conversion functions from different units *to* K
    toK = {'K': lambda val: val,
           'C': lambda val: val + 273.15,
           'F': lambda val: (val + 459.67)*5/9,
          }
    # Dictionary of conversion functions *from* K to different units
    fromK = {'K': lambda val: val,
             'C': lambda val: val - 273.15,
             'F': lambda val: val*9/5 - 459.67,
            }

    # First convert the temperature from from_unit to K
    try:
        T = toK[from_unit](value)
    except KeyError:
        raise ValueError('Unrecognised temperature unit: {}'.format(from_unit))

    if T < 0:
        raise ValueError('Invalid temperature: {} {} is less than 0 K'
                                .format(value, from_unit))

    if from_unit == to_unit:
       # No conversion needed!
        return value

    # Now convert it from K to to_unit and return its value
    try:
        return fromK[to_unit](T)
    except KeyError:
        raise ValueError('Unrecognised temperature unit: {}'.format(to_unit))