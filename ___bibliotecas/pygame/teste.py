

var = 0.1
var2 = 1
# print(str(type(var)).split("'")[1])
# print(str(type(var2)).split("'")[1])


var3 = 0
var4 = 1_000_000

# while True:
#     var3 += 0.25
#     if var3 % var4 == 1:
#         print('OK')

# print(2 % 2 == 1)


class A:

    def x(self):
        return self.x

    def __init__(self):
        self.x = 0


sample = A()
print(sample.x)
