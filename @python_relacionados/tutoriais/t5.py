

"""
Objetivo
    mostrar a diferença de cálculo sequencial com loop for vs loop while vs comprehension
"""
# todo Tutorial 5

def multiplicar_loop_for(valor):
    tabuada = range(1, 11)
    for dados in tabuada:
        print('{:.2f} x {} = {:.2f}'.format(valor, dados, (valor * dados)))

multiplicar_loop_for(9.34)

def subtrair_loop_while(valor, subtrair_a_partir=0):
    # Impedir que o parâmetro 2 da função faça o cálculo errado
    if subtrair_a_partir < 0:
        # se parâmetro negativo
        subtrair_a_partir = abs(subtrair_a_partir)
        # converter pra positivo, pois negativos somam-se, e este não é o objeto da função

    while subtrair_a_partir:
        # enquanto maior que 0, ou seja, enquanto True
        if valor == int(valor):
            # se par 1 inteiro, não converter par1 para flutuante
            print('{} - {} = {:.2f}'.format(valor, subtrair_a_partir, (valor - subtrair_a_partir)))
            subtrair_a_partir -= 1
        else:
            print('{:.2f} - {} = {:.2f}'.format(valor, subtrair_a_partir, (valor - subtrair_a_partir)))
            subtrair_a_partir -= 1

subtrair_loop_while(44, 19)

# par2 = int or float (para permitir variação de parâmetro)
def dividir_por_comprehension(*args, divisor=1 or 1.0):
    if divisor == 0:
        raise ZeroDivisionError('======= Erro =======\nDivisões por zero são impossíveis')
    comprehension = ['\n{:.2f} / {} = {:.2f}\n'.format(dados, divisor, dados/divisor) for dados in args]
    print(*comprehension)

dividir_por_comprehension(12.4, 96, 88.104, 72_466_001, 25, divisor=3.9)
