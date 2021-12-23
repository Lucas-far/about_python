

def mtd_meter_converter(to_type: str, meter_value: float):
    """"""

    measures = 'quilômetro,hectometro,decametro,metro,decímetro,centímetro,milímetro'.split(',')
    # measures = 'kilometer,hectometer,dekameter,meter,decimeter,centimeter,millimeter'.split(',')
    values = [0.001, 0.01, 0.1, 1, 10, 100, 1000]

    counter = 0

    while counter < len(measures):
        if to_type == measures[counter]:
            calculus = meter_value * values[counter]
            frame = f'{meter_value} metros é o equivalente a: {calculus} {to_type}(s)'
            return frame
        else:
            counter += 1


if __name__ == '__main__':
    print(var := mtd_meter_converter(to_type='quilômetro', meter_value=1000))
    print(var2 := mtd_meter_converter(to_type='hectometro', meter_value=1000))
    print(var3 := mtd_meter_converter(to_type='decametro', meter_value=1000))
    print(var4 := mtd_meter_converter(to_type='metro', meter_value=1000))
    print(var5 := mtd_meter_converter(to_type='decímetro', meter_value=1000))
    print(var6 := mtd_meter_converter(to_type='centímetro', meter_value=1000))
    print(var7 := mtd_meter_converter(to_type='milímetro', meter_value=1000))
