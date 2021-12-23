

class Documento:

    @staticmethod
    def gerar_cpf():
        from random import choice
        digits = [*'0.1.2.3.4.5.6.7.8.9'.split('.')]
        splitter_1st = '.'
        splitter_2nd = '-'

        box = []
        start = 0
        total_digits = 11

        while start < total_digits:
            box.append(choice(digits))
            start += 1

        # 030.255.993-08
        box[2] = box[2] + splitter_1st
        box[5] = box[5] + splitter_1st
        box[8] = box[8] + splitter_2nd

        return "".join(box)

    def __init__(self):
        pass


obj = Documento()
print(obj.gerar_cpf())
