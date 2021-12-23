

"""
Objetivo:
    programar uma data final a partir de uma data inicial
"""

import datetime as dt
from datetime import datetime

# @datetime

print(1, agora := datetime.now())
print(2, hr := int(str(agora).split()[1].split(':')[0]))
print(3, mnt := int(str(agora).split()[1].split(':')[1]))
print(4, scnd := round(float(str(agora).split()[1].split(':')[2])))
print(
    5, data_pagamento := dt.datetime.combine(
        (agora + dt.timedelta(days=30)),
        dt.time(hour=hr, minute=mnt, second=scnd)
    ))
