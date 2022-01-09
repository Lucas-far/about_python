

def mtd_temperature_converter(from_type: str, to_type: str, temp_value: float):
    """"""

    if from_type == 'celsius' and to_type == 'fahrenheit':
        from_celsius_to_fahrenheit_calculus = f'{(temp_value * 1.8) + 32:.2f}'
        frame = f'{temp_value} graus Celsius para Fahrenheit: {from_celsius_to_fahrenheit_calculus} graus'
        return frame

    elif from_type == 'celsius' and to_type == 'kelvin':
        from_celsius_to_kelvin_calculus = f'{temp_value + 273.15:.2f}'
        frame = f'{temp_value} graus Celsius para Kelvin: {from_celsius_to_kelvin_calculus} graus'
        return frame

    elif from_type == 'fahrenheit' and to_type == 'celsius':
        from_fahrenheit_to_celsius_calculus = f'{(temp_value - 32) * (5 / 9):.2f}'
        frame = f'{temp_value} graus Fahrenheit para Celsius: {from_fahrenheit_to_celsius_calculus} graus'
        return frame

    elif from_type == 'fahrenheit' and to_type == 'kelvin':
        from_fahrenheit_to_kelvin_calculus = f'{(temp_value - 32) * (5 / 9) + 273.15:.2f}'
        frame = f'{temp_value} graus Fahrenheit para Kelvin: {from_fahrenheit_to_kelvin_calculus} graus'
        return frame

    elif from_type == 'kelvin' and to_type == 'celsius':
        from_kelvin_to_celsius_calculus = f'{temp_value - 273.15:.2f}'
        frame = f'{temp_value} graus Kelvin para Celsius: {from_kelvin_to_celsius_calculus} graus'
        return frame

    elif from_type == 'kelvin' and to_type == 'fahrenheit':
        from_kelvin_to_fahrenheit_calculus = f'{(temp_value - 273.15) * 1.8 + 32:.2f}'
        frame = f'{temp_value} graus Kelvin para Fahrenheit: {from_kelvin_to_fahrenheit_calculus} graus'
        return frame


if __name__ == '__main__':
    print(var := mtd_temperature_converter(from_type='celsius', to_type='fahrenheit', temp_value=125))
    print(var2 := mtd_temperature_converter(from_type='celsius', to_type='kelvin', temp_value=125))
    print(var3 := mtd_temperature_converter(from_type='fahrenheit', to_type='celsius', temp_value=125))
    print(var4 := mtd_temperature_converter(from_type='fahrenheit', to_type='kelvin', temp_value=125))
    print(var5 := mtd_temperature_converter(from_type='kelvin', to_type='celsius', temp_value=125))
    print(var6 := mtd_temperature_converter(from_type='kelvin', to_type='fahrenheit', temp_value=125))
