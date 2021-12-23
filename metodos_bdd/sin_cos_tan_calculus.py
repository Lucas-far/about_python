

def mtd_sin_cos_tan_calculus(measure: str, angle_value: float):
    """"""

    from math import cos, radians, sin, tan

    if measure == 'seno':
        return f'Seno do ângulo de {angle_value} graus: [ {sin(radians(angle_value)):.2f} ]'
    elif measure == 'cosseno':
        return f'Cosseno do ângulo de {angle_value} graus: [ {cos(radians(angle_value)):.2f} ]'
    elif measure == 'tangente':
        return f'Tangente do ângulo de {angle_value} graus: [ {tan(radians(angle_value)):.2f} ]'


if __name__ == '__main__':
    print(var := mtd_sin_cos_tan_calculus(measure='seno', angle_value=90))
    print(var2 := mtd_sin_cos_tan_calculus(measure='cosseno', angle_value=90))
    print(var3 := mtd_sin_cos_tan_calculus(measure='tangente', angle_value=90))
