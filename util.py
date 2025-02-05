# Function that takes either celcius or fahrenheit and converts it to the other

def convert_c_to_f(value):
    return (value * 9/5) + 32

def convert_f_to_c(value):
    return (value - 32) * 5/9

def convert_temperature(value, unit):
    if unit.lower() == 'c':
        return convert_c_to_f(value)
    elif unit.lower() == 'f':
        return convert_f_to_c(value)
    else:
        raise ValueError("Unit must be 'C' or 'F'")