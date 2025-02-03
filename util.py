# Function that takes either celcius or fahrenheit and converts it to the other

def convert_temperature(value, unit):
    if unit.lower() == 'c':
        return convert_c_to_f(value)
    elif unit.lower() == 'f':
        return convert_f_to_c(value)
    else:
        raise ValueError("Unit must be 'C' or 'F'")