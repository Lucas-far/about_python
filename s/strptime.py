

from datetime import datetime
data = datetime.now().strptime('16/07/1992', '%d/%m/%Y')

print(type(data))  # <class 'datetime.datetime'>
print(data)        # 1992-07-16 00:00:00
print(data.day)    # 16
print(data.month)  # 7
print(data.year)   # 1992
