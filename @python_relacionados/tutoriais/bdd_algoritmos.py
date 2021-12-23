""""""

# Adicionador e listador de produtos com rótulação fixa e numeração maleável
"======================================================================================================================"
from resources import *
from ansi_colors import *



ask_for_product = """
{} What product would you like to add? {}
1. Click on the arrow below
2. Type the name of the product 
3. {}Reminder{}: do not use: comma // dot // number // special-character [ only letters and space ]
4. Type 0 to stop adding products 
-> """.format('=' * row, '=' * row, colors['crimson'], colors['standard'])

index = 1
list_products_container = []

while True:
    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break
    while True:
        product = input(ask_for_product)
        label = 'ID {}: '.format(index)
        list_products_container.append(label + product)  # Não é passado apenas o dado da entrada [ strings foram add ]
        index += 1
        if product == '0':
            break
        else:
            print(list_products_container)

    list_products_container.pop()

# =============== Do you wish to stay in this virtual environment? ===============
# 1. Click on the arrow below
# 2. If [ yes ] hit ENTER keyboard key
# 3. If [ no ] type "end" word
# ->
#
# =============== What product would you like to add? ===============
# 1. Click on the arrow below
# 2. Type the name of the product
# 3. Reminder: do not use: comma // dot // number // special-character [ only letters and space ]
# 4. Type 0 to stop adding products
# -> arroz
# ['ID 1: arroz']
"======================================================================================================================"



# Analisador de texto
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_string, string_incompatible_data

name_discard_useless_spacing = None
name_proper_spacing = None
name_proper_grammar = None

title = '\nWelcome to the {}Text analyser{}'.format(
                                                    colors['bold_dodgerblue'],
                                                    colors['standard'])
instructions = """
1. Type some textual data
2. The text will be analysed and it will return a brief report about it"""

ask_for_text = """
{}{} What text do you want to use? {}{}
1. Click on the arrow below
2. Type the text of your desire
3. Hit ENTER
-> """.format(
              '=' * row,
              colors['bold_white'],
              colors['standard'],
              '=' * row)

result = """
Chosen text:            [ {} ]
Text upper cased:       [ {} ]
Text lower cased:       [ {} ] 
Text backwards:         [ {} ]
Text characters length: [ {} ]"""

print(title)
while True:
    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break
    print(title)
    print(instructions)
    while True:
        text = input(ask_for_text)
        for each_data in text:
            if each_data in string_incompatible_data:
                print(mistake_at_string)
                break
            else:
                text_discard_useless_spacing = text.split()
                text_proper_spacing = ' '.join(text_discard_useless_spacing)
                text_proper_grammar = text_proper_spacing.title()

                print(result.format(
                                    text_proper_grammar,
                                    text_proper_grammar.upper(),
                                    text_proper_grammar.lower(),
                                    text_proper_grammar[::-1],
                                    len(text_proper_grammar) - text_proper_grammar.count(' ')
                                    ))
                break
        break
"======================================================================================================================"



# Calculador de hipotenusa
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_float
from math import hypot

title = '\nWelcome to the {}Hypotenuse calculator{}'.format(colors['bold_dodgerblue'], colors['standard'])

instructions = """
{}{} Instructions {}{}
1. In order to calculate the Hypotenuse, it is needed to know: [ opposite angle ] & [ adjacent angle ]
2. It will be asked the opposite angle, type it
3. It will be asked the adjacent angle, type it
4. The hypotenuse will be calculated from the two values provided\n""".format('=' * row, colors['bold_dodgerblue'],
                                                                              colors['standard'], '=' * row)


ask_for_opposite_angle = """
{}{} What is the opposite angle? {}{}
1. {}
2. Type the opposite angle
3. {}
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row, click_arrow, press_enter_key)

ask_for_adjacent_angle = """
{}{} What is the adjacent angle? {}{}
1. {}
2. Type the adjacent angle
3. {}
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row, click_arrow, press_enter_key)

hypotenuse_calculus_report = """
{}{} Hypotenuse calculus report {}{}
Opposite angle provided: {}{:.2f}{}
Adjacent angle provided: {}{:.2f}{}
Result: {}{:.2f}{}\n"""

print(title)

while True:

    algorithm_action = input(doubt_run_algorithm)

    if algorithm_action in algorithm_cease:

        break

    print(title)

    print(instructions)

    while True:

        try:

            opposite_angle = float(input(ask_for_opposite_angle))

            while True:

                try:

                    adjacent_angle = float(input(ask_for_adjacent_angle))

                    print(hypotenuse_calculus_report.format('=' * row, colors['bold_dodgerblue'], colors['standard'],
                                                            '=' * row, colors['bold_crimson'], opposite_angle,
                                                            colors['standard'], colors['bold_dodgerblue'],
                                                            adjacent_angle, colors['standard'],
                                                            colors['bold_yellowgreen'],
                                                            hypot(opposite_angle, adjacent_angle), colors['standard']))
                    break

                except ValueError:

                    print(mistake_at_float)

            break

        except ValueError:

            print(mistake_at_float)
"======================================================================================================================"




# todo -> STANDBY
# prices = [round(uniform(1, 200), 2), round(uniform(1, 200), 2), round(uniform(1, 200), 2), round(uniform(1, 200), 2),
#           round(uniform(1, 200), 2), round(uniform(1, 200), 2), round(uniform(1, 200), 2), round(uniform(1, 200), 2),
#           round(uniform(1, 200), 2), round(uniform(1, 200), 2), round(uniform(1, 200), 2), round(uniform(1, 200), 2),
#           round(uniform(1, 200), 2), round(uniform(1, 200), 2), round(uniform(1, 200), 2), round(uniform(1, 200), 2),
#           round(uniform(1, 200), 2), round(uniform(1, 200), 2), round(uniform(1, 200), 2), round(uniform(1, 200), 2)]
#
# welcome = '\nWelcome to the {}Shopping Kart{}'.format(colors['bold_dodgerblue'], colors['standard'])
#
# products = \
# {
#     '1': {'Product': 'Raquete', 'price:': '{}'.format(prices[0])},
#     '2': {'Product': 'Peteca', 'price:': '{}'.format(prices[1])},
#     '3': {'Product': 'Almofada', 'price:': '{}'.format(prices[2])},
#     '4': {'Product': 'Meia', 'price:': '{}'.format(prices[3])},
#     '5': {'Product': 'Capacete', 'price:': '{}'.format(prices[4])},
#     '6': {'Product': 'Ventilador', 'price:': '{}'.format(prices[5])},
#     '7': {'Product': 'Cama', 'price:': '{}'.format(prices[6])},
#     '8': {'Product': 'Criado-mudo', 'price:': '{}'.format(prices[7])},
#     '9': {'Product': 'Estante', 'price:': '{}'.format(prices[8])},
#     '10': {'Product': 'Cabide', 'price:': '{}'.format(prices[9])},
#     '11': {'Product': 'Martelo', 'price:': '{}'.format(prices[10])},
#     '12': {'Product': 'Quadro', 'price:': '{}'.format(prices[11])},
#     '13': {'Product': 'Porta-retarto', 'price:': '{}'.format(prices[12])},
#     '14': {'Product': 'Mesa', 'price:': '{}'.format(prices[13])},
#     '15': {'Product': 'Ladrilho', 'price:': '{}'.format(prices[14])},
#     '16': {'Product': 'Estátua', 'price:': '{}'.format(prices[15])},
#     '17': {'Product': 'Vidro', 'price:': '{}'.format(prices[16])},
#     '18': {'Product': 'Pia', 'price:': '{}'.format(prices[17])},
#     '19': {'Product': 'Cortina', 'price:': '{}'.format(prices[18])},
#     '20': {'Product': 'Sapato', 'price:': '{}'.format(prices[19])}
# }



# Comparador de inteiros
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_integer

title = '\nWelcome to the {}Integer comparator{}'.format(colors['bold_dodgerblue'], colors['standard'])

menu = """
{}{} Instructions {}{}
Type 2 integers (one by one)
The integers will be compared in order to know if they are twins
""".format('=' * row, colors['bold_dodgerblue'], colors['standard'], '=' * row)

positions = ('1st', '2nd')

reply = ('positive', 'negative', 'none')

ask_for_integer = """
{}{} What is the {} integer to the comparison? {}{}
1. {}
2. Type an integer number
3. {}
-> """

comparison_report = """
{}{} Comparison report {}{}
Numbers to be compared: [ {} vs {} ]
Are they twinned numbers? [ {}{}{} ]
Which one is bigger? [ {}{}{} ]
"""

print(title)

while True:

    algorithm_action = input(doubt_run_algorithm)

    if algorithm_action in algorithm_cease:

        break

    print(title)

    while True:

        try:

            integer = int(input(ask_for_integer.format('=' * row,
                                                       colors['bold_white'],
                                                       positions[0],
                                                       colors['standard'], '=' * row, click_arrow, press_enter_key)))

            while True:

                try:

                    second_integer = int(input(ask_for_integer.format('=' * row,
                                         colors['bold_white'],
                                         positions[1],
                                         colors['standard'], '=' * row, click_arrow, press_enter_key)))

                    if integer > second_integer:

                        print(comparison_report.format('=' * row, colors['bold_dodgerblue'], colors['standard'],
                                                       '=' * row, integer, second_integer, colors['bold_crimson'],
                                                       reply[1], colors['standard'], colors['bold_dodgerblue'],
                                                       integer, colors['standard']))
                        break

                    elif second_integer > integer:

                        print(comparison_report.format('=' * row, colors['bold_dodgerblue'], colors['standard'],
                                                       '=' * row, integer, second_integer, colors['bold_crimson'],
                                                       reply[1], colors['standard'], colors['bold_dodgerblue'],
                                                       second_integer, colors['standard']))
                        break

                    else:

                        print(comparison_report.format('=' * row, colors['bold_dodgerblue'], colors['standard'],
                                                       '=' * row, integer, second_integer, colors['bold_crimson'],
                                                       reply[0], colors['standard'], colors['bold_dodgerblue'],
                                                       reply[2], colors['standard']))
                        break

                except ValueError:

                    print(mistake_at_integer)

            break

        except ValueError:

            print(mistake_at_integer)
"======================================================================================================================"



# Contagem regressiva
"======================================================================================================================"
from time import sleep

for all_numbers in range(10, 0, -1):
    print(end='Processando...{}\n'.format(all_numbers))
    sleep(0.25)
"======================================================================================================================"



# Corretor e selecionador de nomes
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_string, string_incompatible_data

title = '\nWelcome to the {}First and Last name picker{}'.format(colors['dodgerblue'], colors['standard'])

ask_full_name = """
{}{} What is your full name? {}{}
1. Click on the arrow below
2. Type your full name
3. Hit ENTER
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

storage_result = []
first_name = None
last_name = None
result = "\nYour first name is: [ {} ]\nYour last name is: [ {} ]\n"

storage_for_name_adjustment = []
formated_name = None
name_discard_useless_spacing = None
name_proper_spacing = None
name_proper_grammar = None

print(title)
while True:
    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break
    print(title)

    while True:
        full_name = input(ask_full_name)  # !l@u#c$a%s f<a>R,i.a:s     # !lUCAS @fAR#$%ias     # "Lucas# fARI&*()

        name_discard_useless_spacing = full_name.split()
        name_proper_spacing = ' '.join(name_discard_useless_spacing)
        name_proper_grammar = name_proper_spacing.title()

        for each_data in name_proper_grammar:
            if each_data not in string_incompatible_data:

                first_name = name_proper_grammar.split()[0]
                last_name = name_proper_grammar.split().pop()

                print(result.format(first_name, last_name))
                break

            else:
                print(mistake_at_string)
                break
        break
"======================================================================================================================"



# Determinador de número ímpar ou par
"======================================================================================================================"
"Aula:"    # Exercício Python #030 - Par ou Ímpar?
"Link:"    # https://www.youtube.com/watch?v=4vFCzKuHOn4&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=31

from resources import *
from ansi_colors import *
from error_handling import mistake_at_integer

title = '\nWelcome to the {}Even & Odd determiner{}'.format(colors['dodgerblue'], colors['standard'])

informative_message = "\nPlease, type below any integer number in order to know if fits as [ even ] or [ odd ]\n"

ask_for_integer = """
{}{} What integer number do you want to verify? {}{}
1. Click on the arrow below
2. Type an integer number of your desire
3. Hit ENTER
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

report_even = '\nChosen value = [ {} ]\nIs it even or odd? [ even ]\n'
report_odd = '\nChosen value = [ {} ]\nIs it even or odd? [ odd ]\n'

print(title)

while True:
    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break

    print(title)
    print(informative_message)
    while True:
        try:
            integer_value = int(input(ask_for_integer))
            if not integer_value % 2:
                print(report_even.format(integer_value))
                break
            else:
                print(report_odd.format(integer_value))
                break
        except ValueError:
            print(mistake_at_integer)
"======================================================================================================================"



# Gerador de caracteres aleatórios simples
"======================================================================================================================"
from random import choice
alfabeto_unidades = 'abcdefghijklmnopqrstuvwxyz123456789'
# alfabeto = tuple({}.fromkeys('abcdefghijklmnopqrstuvwxyz123456789', None))
var = []
contador = 0
while contador < 100:
    dado = choice(alfabeto_unidades)
    var.extend(dado)
    contador += 1
var = ''.join(var)
print(var)
"======================================================================================================================"



# Gerador de pastas
"======================================================================================================================"
contexto = ['pós-variável']
from os import chdir, getcwd, mkdir

pasta = 0
pastas_criadas = 0
while pasta < 1:
    chdir('C:\\Users\\Lucas\\Desktop\\main')
    mkdir('z')
    chdir(getcwd() + '\\z')
    pasta += 1
    while pastas_criadas <= 6:
        mkdir('pasta' + str(pastas_criadas))
        pastas_criadas += 1
"======================================================================================================================"



# Gerador de tabuada
"======================================================================================================================"
from error_handling import mistake_at_float
from resources import *

title = '\nWelcome to the {}Table Generator{}'.format(colors['dodgerblue'], colors['standard'])

ask_for_float_value = """
1. Click on the arrow below
2. Type an integer value [ positive // negative ]
3. Press ENTER
-> """

multiplier = 1

table_display = "{:.2f} x {} = [ {:.2f} ]"

while True:
    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break

    print(title)

    while True:
        try:
            value = float(input(ask_for_float_value))

            print('\n')
            while multiplier < 10:
                print(table_display.format(value, multiplier, (value * multiplier)))
                multiplier += 1
            break
        except ValueError:
            print(mistake_at_float)
"======================================================================================================================"




# Gerenciador de cédulas
"======================================================================================================================"
from resources import *
from error_handling import mistake_at_integer

title = 'Welcome to the {}Banknote Management{}'.format(colors['dodgerblue'], colors['standard'])

available_banknotes = """
Available banknotes\n 
U$ 100,00\nU$ 50,00\nU$ 20,00\nU$ 10,00\nU$ 5,00\nU$ 2,00\nU$ 1,00
"""

ask_for_banknote = """
{} What is the amount of money that you want to split between the banknotes? {}
1. Click on the arrow below
2. Type the amount of money
3. Hit ENTER
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

banknotes_list = [100, 50, 20, 10, 5, 2, 1]

first_banknote_analysis = None
second_banknote_analysis = None
third_banknote_analysis = None
fourth_banknote_analysis = None
fifth_banknote_analysis = None
sixth_banknote_analysis = None
seventh_banknote_analysis = None

banknote_report = """
Banknote U$ 100 = [ {} ]
Banknote U$ 50  = [ {} ]
Banknote U$ 25  = [ {} ]
Banknote U$ 10  = [ {} ]
Banknote U$ 5   = [ {} ]
Banknote U$ 2   = [ {} ]
Banknote U$ 1   = [ {} ]
"""

print(title)
while True:
    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break
    print(available_banknotes)
    while True:
        try:
            banknote = int(input(ask_for_banknote))

            first_banknote_analysis = banknote // banknotes_list[0]
            banknote %= banknotes_list[0]

            second_banknote_analysis = banknote // banknotes_list[1]
            banknote %= banknotes_list[1]

            third_banknote_analysis = banknote // banknotes_list[2]
            banknote %= banknotes_list[2]

            fourth_banknote_analysis = banknote // banknotes_list[3]
            banknote %= banknotes_list[3]

            fifth_banknote_analysis = banknote // banknotes_list[4]
            banknote %= banknotes_list[4]

            sixth_banknote_analysis = banknote // banknotes_list[5]
            banknote %= banknotes_list[5]

            seventh_banknote_analysis = banknote // banknotes_list[6]
            banknote %= banknotes_list[6]

            print(banknote_report.format(
                                         first_banknote_analysis, second_banknote_analysis, third_banknote_analysis,
                                         fourth_banknote_analysis, fifth_banknote_analysis, sixth_banknote_analysis,
                                         seventh_banknote_analysis))

        except ValueError:
            print(mistake_at_integer)
"======================================================================================================================"



# Gerenciador de salário
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_float

title = "\nWelcome to the {}Salary Management{}\n".format(colors['dodgerblue'], colors['standard'])

ask_for_salary = """
{}{} How much is your current salary? {}{}
1. Click on the arrow below
2. Type how much is your salary
3. Hit ENTER key
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

salary_reference = 1500
raise_fifteen = 0.15
salary_plus_fifteen = 0
raise_ten = 0.10

salary_plus_fifteen_report = """
Your salary has been upgraded from U$ {:.2f} dollars to U$ {}{:.2f}{} dollars
How much is the increase? = {}+ {:.2f}{}"""

salary_plus_ten_report = """
Your salary has been upgraded from U$ {:.2f} dollars to U$ {}{:.2f}{} dollars
How much is the increase? = {}+ {:.2f}{}"""

while True:
    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break
    print(title)
    while True:
        try:
            current_salary = float(input(ask_for_salary))
            if current_salary <= salary_reference:
                salary_plus_fifteen = current_salary + (current_salary * raise_fifteen)
                increase = salary_plus_fifteen - current_salary
                print(salary_plus_fifteen_report.format(current_salary,
                                                        colors['dodgerblue'], salary_plus_fifteen, colors['standard'],
                                                        colors['dodgerblue'], increase, colors['standard']))
                break
            else:
                salary_plus_ten = current_salary + (current_salary * raise_ten)
                increase = salary_plus_ten - current_salary

                print(salary_plus_ten_report.format(current_salary,
                                                    colors['dodgerblue'], salary_plus_ten, colors['standard'],
                                                    colors['dodgerblue'], increase, colors['standard']))
                break
        except ValueError:
            print(mistake_at_float)
"======================================================================================================================"




# Identificador de ano bisexto
"======================================================================================================================"
from resources import *
from ansi_colors import *
from datetime import date
from error_handling import mistake_at_integer

access_date = date.today()
current_year = access_date.year
title = "\nWelcome to the {}Leap year identifier{}".format(colors['dodgerblue'], colors['standard'])

doubt_this_year_leap_year = """
{} Would you like to check if the current year is a leap year? {}
If [ yes ], type 'ok'
If [ no ], hit ENTER
-> """.format('=' * row, '=' * row)

ask_for_year = """
{}{} What is the year that you would like to check? {}{}
1. Click on the arrow below
2. Type a year of your desire
3. Hit ENTER to see the outcome
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

positive = ['ok']

divisible_by_four = 4
divisible_by_hundred = 100
divisible_by_four_hundred = 400

print(title)
while True:
    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break
    print(title)

    this_year_checkage = input(doubt_this_year_leap_year)

    "Exemplo de uma condição composta"
    if this_year_checkage in positive:

        if not current_year % divisible_by_four \
            and current_year % divisible_by_hundred \
                or not current_year % divisible_by_four_hundred:

            print('\nYes, the year [ {} ] is a leap year'.format(current_year))
        else:
            print('No, [ {} ] is not leap year'.format(current_year))

    while True:
        try:
            year_to_scan = int(input(ask_for_year))

            if not year_to_scan % divisible_by_four \
                and year_to_scan % divisible_by_hundred \
                    or not year_to_scan % divisible_by_four_hundred:

                print('\nYes, the year [ {} ] is a leap-year'.format(year_to_scan))
                break

            else:
                print('\nNo, it is not')
                break

        except ValueError:
            print(mistake_at_integer)
"======================================================================================================================"



# Identificador de massa corpórea
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_float, error_invalid_data

algorithm_action = None
data_weight = None
data_height = None
body_mass_index_result = None

morbid_obesity_aesthetics = ()
obesity_aesthetics = ()
overweight_aesthetics = ()
average_aesthetics = ()
lacking_aesthetics = ()

measures = ('weight', 'height')
instructions_aesthetics = (row, colors['dodgerblue'], colors['standard'], row)
get_data_weigth_aesthetics = (row, colors['bold_white'], measures[0], colors['standard'], row, click_arrow, measures[0],
                              press_enter_key)
get_data_height_aesthetics = (row, colors['bold_white'], measures[1], colors['standard'], row, click_arrow, measures[1],
                              press_enter_key)

ask_for_data = """
{}{} What is your current {}? {}{}
1. {}
2. Type you current {}
3. {}
-> """

warnings = ('{}Dangerous{} hint: exercise and immediate change of diet!'
            .format(colors['bold_crimson'], colors['standard']),
            '{}Worrisome{} hint: exercise and gradual change of diet!'
            .format(colors['bold_crimson'], colors['standard']),
            '{}Fairly bad{} hint: exercise and consider change of diet'
            .format(colors['crimson'], colors['standard']),
            '{}Average{} hint: you are alright, just keep on this way!'
            .format(colors['bold_dodgerblue'], colors['standard']),
            '{}Lacking{} hint: you need more body weight!'
            .format(colors['bold_yellowgreen'], colors['standard']))

condition = ('{}morbid obesity{}'.format(colors['bold_crimson'], colors['standard']),
             '{}obesity{}'.format(colors['bold_crimson'], colors['standard']),
             '{}overweight{}'.format(colors['crimson'], colors['standard']),
             '{}average{}'.format(colors['bold_dodgerblue'], colors['standard']),
             '{}lacking{}'.format(colors['bold_yellowgreen'], colors['standard']))

body_mass_index_report_text = """
{}{} Body mass index report {}{}
1. Person's weight provided: [ {} ]
2. Person's height provided: [ {} ]
3. Body mass index value:    [ {:.2f} ]
4. Health status:            [ {} ]
5. Health condition:         [ {} ]
"""


def welcome():
    print('\nWelcome to the {}Body mass index identifier{}'.format(colors['bold_yellowgreen'], colors['standard']))


def algorithm_start():
    global algorithm_action

    algorithm_action = input(doubt_run_algorithm)


def instructions():
    print("""
{}{} Instructions {}{}
1. Provide your weight data
2. Provide your height data
3. The algorithm will provide your body mass index
4. You will be warned to what kind of procedure is the rightest for you
""".format(*instructions_aesthetics))


def get_data_weigth():
    global data_weight

    data_weight = float(input(ask_for_data.format(*get_data_weigth_aesthetics)))


def get_data_height():
    global data_height

    data_height = float(input(ask_for_data.format(*get_data_height_aesthetics)))


def body_mass_index_calculator(weight, height):
    global body_mass_index_result

    body_mass_index_result = weight / height ** 2


def body_mass_index_report():
    global body_mass_index_report_text, morbid_obesity_aesthetics, obesity_aesthetics, overweight_aesthetics, \
           average_aesthetics, lacking_aesthetics

    if body_mass_index_result >= 40:

        morbid_obesity_aesthetics = (row, colors['bold_yellowgreen'], colors['standard'], row, data_weight, data_height,
                                     body_mass_index_result, condition[0], warnings[0])
        print(body_mass_index_report_text.format(*morbid_obesity_aesthetics))

    elif 30 <= body_mass_index_result < 40:

        obesity_aesthetics = (row, colors['bold_yellowgreen'], colors['standard'], row, data_weight, data_height,
                              body_mass_index_result, condition[1], warnings[1])
        print(body_mass_index_report_text.format(*obesity_aesthetics))

    elif 25 <= body_mass_index_result < 30:

        overweight_aesthetics = (row, colors['bold_yellowgreen'], colors['standard'], row, data_weight, data_height,
                                 body_mass_index_result, condition[2], warnings[2])
        print(body_mass_index_report_text.format(*overweight_aesthetics))

    elif 18.5 <= body_mass_index_result < 25:

        average_aesthetics = (row, colors['bold_yellowgreen'], colors['standard'], row, data_weight, data_height,
                              body_mass_index_result, condition[3], warnings[3])
        print(body_mass_index_report_text.format(*average_aesthetics))

    elif body_mass_index_result < 18.5:

        lacking_aesthetics = (row, colors['bold_yellowgreen'], colors['standard'], row, data_weight, data_height,
                              body_mass_index_result, condition[4], warnings[4])
        print(body_mass_index_report_text.format(*lacking_aesthetics))

welcome()
while True:
    algorithm_start()
    if algorithm_action in algorithm_cease:
        break

    while True:
        instructions()
        try:
            get_data_weigth()

            while data_weight <= 0:
                instructions()
                print(error_invalid_data)
                get_data_weigth()
            else:
                break

        except ValueError:
            print(mistake_at_float)

    while True:
        instructions()
        try:
            get_data_height()

            while data_height <= 0:
                instructions()
                print(error_invalid_data)
                get_data_height()
            else:

                body_mass_index_calculator(data_weight, data_height)
                body_mass_index_report()
                break

        except ValueError:
            print(mistake_at_float)
"======================================================================================================================"



# Identificador de signos
"======================================================================================================================"
"""
Requirements
------------

1. datetime       (to get current date, custom date, get date month)
2. error_handling (module to treat alternative errors)
3. resources      (module to write less code)
4. time           (to create intervals of texts)
"""

from datetime import datetime, MAXYEAR
from error_handling import mistake_at_integer, error_invalid_data
from resources import *
from time import sleep


input_algorithm_procedure = None
input_birth_day = None
input_birth_month = None
input_birth_year = None

date_today = None
my_birth = None
my_birth_month = None
my_date_string = None
my_existence_calculus = None
my_lifetime = None
signs = ()
capricorn, aquarius, pisces, aries, taurus, gemini, cancer, leo, virgo, libra, scorpio, sagittarius = \
    None, None, None, None, None, None, None, None, None, None, None, None
report_text = None


def welcome():
    """To return welcome message and name of the algorithm (str).

    :return text.format(*design)"""

    text = '\nWelcome to the {}Sign identifier{}'

    design = (colors['bold_dodgerblue'], colors['standard'])

    return text.format(*design)

skeleton = (colors['bold_goldenrod'], colors['standard'], welcome.__doc__)
welcome_doc = "\n{}welcome(){}\n{}".format(*skeleton)
print(welcome_doc)


def start():
    """To return input (str) to ask if user wants to run algorithm or not.
    - If user provides (str) 'end': break.
    - Else: continue.

    :return input_algorithm_procedure
    """
    global input_algorithm_procedure

    input_algorithm_procedure = input(doubt_run_algorithm)

    return input_algorithm_procedure

skeleton2 = (colors['bold_goldenrod'], colors['standard'], start.__doc__)
start_doc = "\n{}start(){}\n{}".format(*skeleton2)
print(start_doc)


def instructions():
    """To return instructions (str) which the algorithm performs.

    :return text.format(*design)
    """

    text = """
    {}{} Instructions {}{}
    1. Inform your birth in brazilian date method
    2. What is the order? {}day/month/year{} [ dd/mm/yyyy ]
    3. The algorithm will report:
        -> user's {}birth date{}
        -> user's {}sign{}
        -> user's {}days of living{}    
    """

    design = (row, colors['bold_dodgerblue'], colors['standard'], row, colors['bold_white'], colors['standard'],
              colors['bold_white'], colors['standard'], colors['bold_white'], colors['standard'],
              colors['bold_white'], colors['standard'], colors['bold_white'], colors['standard'])

    return text.format(*design)

skeleton3 = (colors['bold_goldenrod'], colors['standard'], instructions.__doc__)
instructions_doc = "\n{}instructions(){}\n{}".format(*skeleton3)
print(instructions_doc)


def get_birth_day():
    """To place two loops to control errors and gather user's day of birth input.
    - If user provides (int) == 1 to 31:                          break.
    - If user provides (int) != 1 to 31:                          print(var_custom_error)
    - If user provides (not all number/ not number) (ValueError): print(var_custom_error).
    - Else:                                                       break.
    """
    global input_birth_day

    step = '\n{}STEP 1 - Provide your birth day{}'.format(colors['bold_yellowgreen'], colors['standard'])

    text = """
    {} {}In what{} {}day{} {}have you been born?{} [ 1 to 31 ] {}
    1. {}
    2. Type the day you have been born
    3. {}
    -> """

    design = (row, colors['bold_white'], colors['standard'], colors['bold_dodgerblue'], colors['standard'],
              colors['bold_white'], colors['standard'], row, click_arrow, press_enter_key)

    while True:  # to keep user from providing wrong type data (not number only)
        try:
            print(step)
            input_birth_day = int(input(text.format(*design)))
            while input_birth_day <= 0 or input_birth_day > 31:  # to keep user from providing improper data
                print(error_invalid_data)
                get_birth_day()
            else:
                break
        except ValueError:
            print(mistake_at_integer)

skeleton4 = (colors['bold_goldenrod'], colors['standard'], get_birth_day.__doc__)
get_birth_day_doc = "\n{}get_birth_day(){}\n{}".format(*skeleton4)
print(get_birth_day_doc)


def get_birth_month():
    """To place two loops to control errors and gather user's month of birth input.
    - If user provides (int) == 1 to 12:                          break.
    - If user provides (int) != 1 to 12:                          print(var_custom_error)
    - If user provides (not all number/ not number) (ValueError): print(var_custom_error).
    - Else:                                                       break.
    """
    global input_birth_month
    step = '\n{}STEP 2 - Provide your birth month{}'.format(colors['bold_yellowgreen'], colors['standard'])
    design = (row, colors['bold_white'], colors['standard'], colors['bold_dodgerblue'], colors['standard'],
              colors['bold_white'], colors['standard'], row, click_arrow, press_enter_key)
    text = """
    {} {}What is the{} {}number of the month{} {}that you have been born?{} [ 1 ] to [ 12 ] {}
    1. {}
    2. Type the month that you have been born
    3. {}
    -> """

    while True:  # to keep user from providing wrong type data (not number only)
        try:
            print(step)
            input_birth_month = int(input(text.format(*design)))
            while input_birth_month < 1 or input_birth_month > 12:  # to keep user from providing improper data
                print(error_invalid_data)
                get_birth_month()
            else:
                break
        except ValueError:
            print(mistake_at_integer)

skeleton5 = (colors['bold_goldenrod'], colors['standard'], get_birth_month.__doc__)
get_birth_month_doc = "\n{}get_birth_month(){}\n{}".format(*skeleton5)
print(get_birth_month_doc)


def get_birth_year():
    """To place two loops to control errors and gather user's year of birth input.
    - If user provides (int) == 1 to 9999:                        break.
    - If user provides (int) < 1 or > 9999:                       print(var_custom_error).
    - If user provides (not all number/ not number) (ValueError): print(var_custom_error).
    - Else:                                                       break.
    """

    global input_birth_year

    step = '\n{}STEP 3 - Provide your birth month{}'.format(colors['bold_yellowgreen'], colors['standard'])

    text = """
    {} {}In what{} {}year{} {}have you been born?{} {}
    1. {}
    2. Type the year that you have been born
    3. {}
    -> """

    design = (row, colors['bold_white'], colors['standard'], colors['bold_dodgerblue'], colors['standard'],
              colors['bold_white'], colors['standard'], row, click_arrow, press_enter_key)

    deadline = MAXYEAR  # Python deadline for date is 9999

    while True:  # to keep user from providing wrong type data (not number only)
        try:
            print(step)
            input_birth_year = int(input(text.format(*design)))
            while input_birth_year <= 0 or input_birth_year > deadline:  # to keep user from providing improper data
                print(error_invalid_data)
                get_birth_year()
            else:
                break
        except ValueError:
            print(mistake_at_integer)

skeleton6 = (colors['bold_goldenrod'], colors['standard'], get_birth_year.__doc__)
get_birth_year_doc = "\n{}get_birth_year(){}\n{}".format(*skeleton6)
print(get_birth_year_doc)


def get_date_today():
    """To get and store real time full date data (year, month, day, hour, minute, second, microsecond)"""

    global date_today

    date_today = datetime.now()

skeleton7 = (colors['bold_goldenrod'], colors['standard'], get_date_today.__doc__)
get_date_today_doc = "\n{}get_date_today(){}\n{}".format(*skeleton7)
print(get_date_today_doc)


def custom_birth_date_get_birth_month():
    """To custom and store user's birthday (user's year input, user's month input, user's second input)
    To get and store user's month for later use in condition
    """

    global my_birth, my_birth_month

    my_birth = datetime(input_birth_year, input_birth_month, input_birth_day)

    my_birth_month = my_birth.month

skeleton8 = (colors['bold_goldenrod'], colors['standard'], custom_birth_date_get_birth_month.__doc__)
custom_birth_date_get_birth_month_doc = "\n{}custom_birth_date_get_birth_month(){}\n{}".format(*skeleton8)
print(custom_birth_date_get_birth_month_doc)


def design_str_birth_date():
    """To custom and store user's full birthday by using a string"""

    global my_date_string

    my_date_string = str(input_birth_year) + '/' + str(input_birth_month) + '/' + str(input_birth_day)

skeleton9 = (colors['bold_goldenrod'], colors['standard'], design_str_birth_date.__doc__)
design_str_birth_date_doc = "\n{}design_str_birth_date(){}\n{}".format(*skeleton9)
print(design_str_birth_date_doc)


def calculate_plus_design_lifetime():
    """To calculate and store user's lifetime and design it into a string"""

    global my_existence_calculus, my_lifetime

    my_existence_calculus = date_today - my_birth

    my_lifetime = 'About {} days'.format(str(my_existence_calculus).split()[0])

skeleton10 = (colors['bold_goldenrod'], colors['standard'], calculate_plus_design_lifetime.__doc__)
calculate_plus_design_lifetime_doc = "\n{}calculate_plus_design_lifetime(){}\n{}".format(*skeleton10)
print(calculate_plus_design_lifetime_doc)


def create_signs_container():
    """To create and store signs (str) into a tuple for later access"""

    global signs

    signs = (None, 'Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra',
             'Scorpio', 'Saggitarius')

skeleton12 = (colors['bold_goldenrod'], colors['standard'], create_signs_container.__doc__)
create_signs_container_doc = "\n{}create_signs_container(){}\n{}".format(*skeleton12)
print(create_signs_container_doc)


def system_texts():
    """To display procedures of the algorithm to the final user"""

    print('\nGetting current date...'), sleep(1)
    print("Scanning user's month..."), sleep(1)
    print("Customizing user's date..."), sleep(1)
    print("Calculating user's day of living..."), sleep(1)
    print("Designing user's day of living..."), sleep(1)
    print("Finding user's sign..."), sleep(1)
    print("Ready!\n")

skeleton14 = (colors['bold_goldenrod'], colors['standard'], system_texts.__doc__)
system_texts_doc = "\n{}system_texts(){}\n{}".format(*skeleton14)
print(system_texts_doc)


def custom_conditions_throw_result():
    """To custom skeleton (str) and its components in order to throw the final result of the algorithm"""

    global report_text, capricorn, aquarius, pisces, aries, taurus, gemini, cancer, leo, virgo, libra, scorpio,\
        sagittarius

    report_text = """
    {}{} Report {}{}
    Your birthy date:    [ {} ]
    Your sign is:        [ {} ]
    Your days of living: [ {} ]    
    """

    capricorn = (row, colors['bold_white'], colors['standard'], row, my_date_string, signs[1], my_lifetime)
    aquarius = (row, colors['bold_white'], colors['standard'], row, my_date_string, signs[2], my_lifetime)
    pisces = (row, colors['bold_white'], colors['standard'], row, my_date_string, signs[3], my_lifetime)
    aries = (row, colors['bold_white'], colors['standard'], row, my_date_string, signs[4], my_lifetime)
    taurus = (row, colors['bold_white'], colors['standard'], row, my_date_string, signs[5], my_lifetime)
    gemini = (row, colors['bold_white'], colors['standard'], row, my_date_string, signs[6], my_lifetime)
    cancer = (row, colors['bold_white'], colors['standard'], row, my_date_string, signs[7], my_lifetime)
    leo = (row, colors['bold_white'], colors['standard'], row, my_date_string, signs[8], my_lifetime)
    virgo = (row, colors['bold_white'], colors['standard'], row, my_date_string, signs[9], my_lifetime)
    libra = (row, colors['bold_white'], colors['standard'], row, my_date_string, signs[10], my_lifetime)
    scorpio = (row, colors['bold_white'], colors['standard'], row, my_date_string, signs[11], my_lifetime)
    sagittarius = (row, colors['bold_white'], colors['standard'], row, my_date_string, signs[12], my_lifetime)

    is_capricorn1 = [True if input_birth_day in range(22, 32) and my_birth_month == 12 else None]
    is_capricorn2 = [True if input_birth_day in range(1, 21) and my_birth_month == 1 else None]
    is_aquarius1 = [True if input_birth_day in range(21, 32) and my_birth_month == 1 else None]
    is_aquarius2 = [True if input_birth_day in range(1, 19) and my_birth_month == 2 else None]
    is_pisces1 = [True if input_birth_day in range(19, 32) and my_birth_month == 2 else None]
    is_pisces2 = [True if input_birth_day in range(1, 21) and my_birth_month == 3 else None]
    is_aries1 = [True if input_birth_day in range(21, 32) and my_birth_month == 3 else None]
    is_aries2 = [True if input_birth_day in range(1, 21) and my_birth_month == 4 else None]
    is_taurus1 = [True if input_birth_day in range(21, 32) and my_birth_month == 4 else None]
    is_taurus2 = [True if input_birth_day in range(1, 21) and my_birth_month == 5 else None]
    is_gemini1 = [True if input_birth_day in range(21, 32) and my_birth_month == 5 else None]
    is_gemini2 = [True if input_birth_day in range(1, 21) and my_birth_month == 6 else None]
    is_cancer1 = [True if input_birth_day in range(21, 32) and my_birth_month == 6 else None]
    is_cancer2 = [True if input_birth_day in range(1, 23) and my_birth_month == 7 else None]
    is_leo1 = [True if input_birth_day in range(23, 32) and my_birth_month == 7 else None]
    is_leo2 = [True if input_birth_day in range(1, 23) and my_birth_month == 8 else None]
    is_virgo1 = [True if input_birth_day in range(23, 32) and my_birth_month == 8 else None]
    is_virgo2 = [True if input_birth_day in range(1, 23) and my_birth_month == 9 else None]
    is_libra1 = [True if input_birth_day in range(23, 32) and my_birth_month == 9 else None]
    is_libra2 = [True if input_birth_day in range(1, 23) and my_birth_month == 10 else None]
    is_scorpio1 = [True if input_birth_day in range(23, 32) and my_birth_month == 10 else None]
    is_scorpio2 = [True if input_birth_day in range(1, 22) and my_birth_month == 11 else None]
    is_sagittarius1 = [True if input_birth_day in range(22, 32) and my_birth_month == 11 else None]
    is_sagittarius2 = [True if input_birth_day in range(1, 22) and my_birth_month == 12 else None]

    if is_capricorn1[0] or is_capricorn2[0]:        # Capricorn:   from 22 december  to 20 january
        print(report_text.format(*capricorn))
    elif is_aquarius1[0] or is_aquarius2[0]:        # Aquarius:    from 21 january   to 18 february
        print(report_text.format(*aquarius))
    elif is_pisces1[0] or is_pisces2[0]:            # Pisces:      from 19 february  to 20 march
        print(report_text.format(*pisces))
    elif is_aries1[0] or is_aries2[0]:              # Aries:       from 21 march     to 20 april
        print(report_text.format(*aries))
    elif is_taurus1[0] or is_taurus2[0]:            # Taurus:      from 21 april     to 20 may
        print(report_text.format(*taurus))
    elif is_gemini1[0] or is_gemini2[0]:            # Gemini:      from 21 may       to 20 june
        print(report_text.format(*gemini))
    elif is_cancer1[0] or is_cancer2[0]:            # Cancer:      from 21 june      to 22 july
        print(report_text.format(*cancer))
    elif is_leo1[0] or is_leo2[0]:                  # Leo:         from 23 july      to 22 august
        print(report_text.format(*leo))
    elif is_virgo1[0] or is_virgo2[0]:              # Virgo:       from 23 august    to 22 september
        print(report_text.format(*virgo))
    elif is_libra1[0] or is_libra2[0]:              # Libra:       from 23 september to 22 october
        print(report_text.format(*libra))
    elif is_scorpio1[0] or is_scorpio2[0]:          # Scorpio:     from 23 october   to 21 november
        print(report_text.format(*scorpio))
    elif is_sagittarius1[0] or is_sagittarius2[0]:  # Sagittarius: from 22 november  to 21 december
        print(report_text.format(*sagittarius))

skeleton15 = (colors['bold_goldenrod'], colors['standard'], custom_conditions_throw_result.__doc__)
custom_conditions_throw_result_doc = "\n{}custom_conditions_throw_result(){}\n{}".format(*skeleton15)
print(custom_conditions_throw_result_doc)

print(welcome())
while True:  # to start over the algorithm and ask if it must continue
    start()
    if input_algorithm_procedure in algorithm_cease:
        break
    print(instructions())
    get_birth_day()
    get_birth_month()
    get_birth_year()
    get_date_today()
    custom_birth_date_get_birth_month()
    design_str_birth_date()
    calculate_plus_design_lifetime()
    create_signs_container()
    system_texts()
    custom_conditions_throw_result()
"======================================================================================================================"



# Identificador de tipo de triângulo
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_integer, error_invalid_data

first_triangle = None
second_triangle = None
third_triangle = None
algorithm_action = None
first_choice_aesthetics = None
second_choice_aesthetics = None
third_choice_aesthetics = None

triangles = ('{}equilateral{}'.format(colors['dodgerblue'], colors['standard']),
             '{}isosceles{}'.format(colors['dark_cyan'], colors['standard']),
             '{}scalene{}'.format(colors['yellowgreen'], colors['standard']))

triangles_order = ('{}first{}'.format(colors['dodgerblue'], colors['standard']),
                   '{}second{}'.format(colors['dark_cyan'], colors['standard']),
                   '{}third{}'.format(colors['yellowgreen'], colors['standard']))

ask_for_triangle = """
{}{} What is the size of the {} triangle? {}{}
1. {}
2. Type the size of the {} triangle
3. {}
-> """

triangle_type_report = """
{}{} Triangle type report {}{}
1. Size of the triangles collected: [ {} ] [ {} ] [ {} ]
2. What kind of triangle can be generated? [ {} ]
"""


def welcome():
    print('\nWelcome to the {}Triangle type identifier{}'.format(colors['bold_dodgerblue'], colors['standard']))


def algorithm_start():
    global algorithm_action

    welcome()
    algorithm_action = input(doubt_run_algorithm)


def instructions():
    global triangles

    print("""
{}{} Instructions {}{}
1. Provide three sizes for the triangle (one at once) (integer value) 
2. The algorithm will report the kind of triangle you can create
3. Triangle types: {}{}{} {}{}{} {}{}{}
""".format(row, colors['bold_white'], colors['standard'], row,
           colors['dodgerblue'], triangles[0], colors['standard'],
           colors['dodgerblue'], triangles[1], colors['standard'],
           colors['dodgerblue'], triangles[2], colors['standard']))


def get_first_triangle_value():
    global first_triangle, ask_for_triangle

    first_triangle = int(input(ask_for_triangle.format(row, colors['bold_white'], triangles_order[0],
                                                       colors['standard'], row, click_arrow,
                                                       triangles_order[0], press_enter_key)))


def get_second_triangle_value():
    global second_triangle, ask_for_triangle

    second_triangle = int(input(ask_for_triangle.format(row, colors['bold_white'], triangles_order[1],
                                                        colors['standard'], row, click_arrow,
                                                        triangles_order[1], press_enter_key)))


def get_third_triangle_value():
    global third_triangle, ask_for_triangle

    third_triangle = int(input(ask_for_triangle.format(row, colors['bold_white'], triangles_order[2],
                                                       colors['standard'], row, click_arrow,
                                                       triangles_order[2], press_enter_key)))


def triangle_type_determiner():
    global first_choice_aesthetics, second_choice_aesthetics, third_choice_aesthetics

    if first_triangle == second_triangle == third_triangle:

        first_choice_aesthetics = (row, colors['bold_yellowgreen'], colors['standard'], row, first_triangle,
                                   second_triangle, third_triangle, triangles[0])

        print(triangle_type_report.format(*first_choice_aesthetics))

    elif first_triangle == second_triangle or first_triangle == third_triangle:

        second_choice_aesthetics = (row, colors['bold_yellowgreen'], colors['standard'], row, first_triangle,
                                    second_triangle, third_triangle, triangles[1])

        print(triangle_type_report.format(*second_choice_aesthetics))

    elif first_triangle != second_triangle != third_triangle:

        third_choice_aesthetics = (row, colors['bold_yellowgreen'], colors['standard'], row, first_triangle,
                                   second_triangle, third_triangle, triangles[2])

        print(triangle_type_report.format(*third_choice_aesthetics))


while True:
    algorithm_start()
    if algorithm_action in algorithm_cease:
        break

    while True:
        instructions()
        try:
            get_first_triangle_value()

            while first_triangle <= 0:
                instructions()
                print(error_invalid_data)
                get_first_triangle_value()
            else:
                break

        except ValueError:
            print(mistake_at_integer)

    while True:
        try:
            instructions()
            get_second_triangle_value()

            while second_triangle <= 0:
                instructions()
                print(error_invalid_data)
                get_second_triangle_value()
            else:
                break

        except ValueError:
            print(mistake_at_integer)

    while True:
        try:
            instructions()
            get_third_triangle_value()

            while third_triangle <= 0:
                instructions()
                print(error_invalid_data)
                get_third_triangle_value()
            else:
                triangle_type_determiner()
                break

        except ValueError:
            print(mistake_at_integer)
"======================================================================================================================"



# Jogo de adivinhação de números inteiros
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_integer
from random import choice, shuffle


title = '\nWelcome to the {}Guessing numbers game{}'.format(colors['dodgerblue'], colors['standard'])

ask_for_integer = """
{}{} What is the integer number that you are thinking at the moment? {}{}
1. Click on the arrow below
2. Type any integer number [ + or - ]
3. Press ENTER keyboard key""".format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

algorithm_number_choice = None

five_backwards = 5

six_forwards = 6

in_game_numbers = []

failure = "\nYou thought about number [ {} ]\nbut I thought about number [ {} ] instead :(\n"

success = "\nWe thought about the same number, number [ {} ], congratulations :)\n"

print(title)
while True:
    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break
    print(title)
    while True:
        try:
            integer = int(input(ask_for_integer))

            in_game_numbers.extend(list(range((integer - five_backwards), (integer + six_forwards))))

            shuffle(in_game_numbers)

            algorithm_number_choice = choice(in_game_numbers)

            if algorithm_number_choice == integer:
                print('\nIn-game numbers {}:'.format(in_game_numbers))
                print(success.format(integer))
                in_game_numbers.clear()
                break
            else:
                print('\nIn-game numbers: {}'.format(in_game_numbers))
                print(failure.format(integer, algorithm_number_choice))
                in_game_numbers.clear()
                break

        except ValueError:
            print(mistake_at_integer)
"======================================================================================================================"



# Jogo de pedra - papel - tesoura
"======================================================================================================================"
from error_handling import error_invalid_data, mistake_at_integer
from resources import *
from random import randint
from time import sleep

input_algorithm_procedure = None
input_chosen_option = None

game_syllable = ('\nJO', 'KEN', 'PO')
index = randint(0, 2)
objects = ('ROCK', 'PAPER', 'SCISSORS')
randomizer = objects[index]


def welcome():
    design = (colors['bold_dodgerblue'], colors['standard'])
    text = '\nWelcome to the {}ROCK | PAPER | SCISSORS{}'
    return text.format(*design)


def instructions():
    design = (row, colors['bold_white'], colors['standard'], row)
    text = """
{}{} Instructions {}{}
1. Provide the input corresponding to an object of the game
2. The algorithm will choose its own object
3. The report of who won/draw will be displayed
"""
    return text.format(*design)


def start():
    global input_algorithm_procedure
    input_algorithm_procedure = input(doubt_run_algorithm)
    return input_algorithm_procedure


def menu():
    design = (row, colors['bold_dark_cyan'], colors['standard'], row)
    text = """
{}{} Menu options {}{}
Insert one of these numbers at the input below
[ 0 ] ROCK
[ 1 ] PAPER
[ 2 ] SCISSORS
"""
    return text.format(*design)


def chosen_object():
    global input_chosen_option
    design = (row, colors['bold_white'], colors['standard'], row, click_arrow, press_enter_key)
    text = """
{}{} What object will you select, [ 0 ] [ 1 ] or [ 2 ]? {}{}
1. {}
2. Type objects from 0 to 2
3. {}
"""
    input_chosen_option = int(input(text.format(*design)))
    return input_chosen_option


def conditions():
    text = """
{}{} Result report {}{}
1. Gamer's choice:     [ {} ]
2. Algorithm's choice: [ {} ]
3. Result:             [ {} ]   
"""
    defeat = ('You lose :(',)
    draw = ('Draw, fair enough u_u',)
    victory = ('Victory, nice :)',)

    defeat_rock = (row, colors['bold_dodgerblue'], colors['standard'], row, 'ROCK', 'PAPER', defeat[0])
    draw_rock = (row, colors['bold_dodgerblue'], colors['standard'], row, 'ROCK', 'ROCK', draw[0])
    victory_rock = (row, colors['bold_dodgerblue'], colors['standard'], row, 'ROCK', 'SCISSORS', victory[0])

    defeat_paper = (row, colors['bold_dodgerblue'], colors['standard'], row, 'PAPER', 'SCISSORS', defeat[0])
    draw_paper = (row, colors['bold_dodgerblue'], colors['standard'], row, 'PAPER', 'PAPER', draw[0])
    victory_paper = (row, colors['bold_dodgerblue'], colors['standard'], row, 'PAPER', 'ROCK', victory[0])

    defeat_scissors = (row, colors['bold_dodgerblue'], colors['standard'], row, 'SCISSORS', 'ROCK', defeat[0])
    draw_scissors = (row, colors['bold_dodgerblue'], colors['standard'], row, 'SCISSORS', 'SCISSORS', draw[0])
    victory_scissors = (row, colors['bold_dodgerblue'], colors['standard'], row, 'SCISSORS', 'PAPER', victory[0])


    if input_chosen_option == 0:

        if randomizer == 'ROCK':
            print(text.format(*draw_rock))
        elif randomizer == 'PAPER':
            print(text.format(*defeat_rock))
        elif randomizer == 'SCISSORS':
            print(text.format(*victory_rock))

    elif input_chosen_option == 1:

        if randomizer == 'ROCK':
            print(text.format(*victory_paper))
        elif randomizer == 'PAPER':
            print(text.format(*draw_paper))
        elif randomizer == 'SCISSORS':
            print(text.format(*defeat_paper))

    elif input_chosen_option == 2:

        if randomizer == 'ROCK':
            print(text.format(*defeat_scissors))
        elif randomizer == 'PAPER':
            print(text.format(*victory_scissors))
        elif randomizer == 'SCISSORS':
            print(text.format(*draw_scissors))

print(welcome())
print(instructions())
while True:
    start()
    if input_algorithm_procedure in algorithm_cease:
        break
    while True:
        try:
            print(menu())
            chosen_object()
            while input_chosen_option < 0 or input_chosen_option > 2:
                print(instructions())
                print(error_invalid_data)
                chosen_object()
            else:
                for each_data in game_syllable:
                    print(each_data)
                    sleep(0.4)
                conditions()
                break
        except ValueError:
            print(mistake_at_integer)
"======================================================================================================================"



# Organizador e contador de caracteres de palavras
"======================================================================================================================"
text = input('Informe o seu texto aqui, por favor\n-> ')

# LuCAs faRIAS   SANtoS [ Exemplo de dado bagunçado para tratar ]
text_discard_unnecessary_spacing = text.split()
text_proper_spacing = ' '.join(text_discard_unnecessary_spacing)
text_proper_grammar = text_proper_spacing.title()
text_proper_grammar_list = text_proper_grammar.split()

for dado in text_proper_grammar_list:
    if ',' in dado:
        print('[ {} ] = [ {} caracteres ]'.format(dado, len(dado) - dado.count(',')))  # Evitar a contagem da [ , ]
    else:
        print('[ {} ] = [ {} caracteres ]'.format(dado, len(dado)))
"======================================================================================================================"



# Perseguidor de número inteiro
"======================================================================================================================"
from random import shuffle
from time import sleep
from ansi_colors import colors

algorithm_procedure = None

row = 15

doubt_run_algorithm = """
{} Do you wish to stay in this virtual environment? {}
1. Click on the arrow below
2. If [ yes ] hit ENTER keyboard key
3. If [ no ] type "end" word
-> """.format('=' * row, '=' * row)

algorithm_cease = ['end']

welcome = "\nWelcome to the {}Integer number seeker{}\n".format(colors['dodgerblue'], colors['standard'])

instructions = """
{} Instructions {}
1. Provide a range between two integer numbers [ smaller to bigger ]
2. Provide a 3rd integer number that you want to find between this range
3. The algorithm will randomize the values and the indexes of the values
4. By the end, it will inform you where your desired number has been found\n""".format('=' * row, '=' * row)

ask_range_first_integer = """
{} What is the 1st value of the range? {}
1. Click on the arrow below
2. Type an integer value [ no comma, no dot, no special characters, only numbers ]
-> """.format('=' * row, '=' * row)

ask_range_second_integer = """
{} What is the 2nd integer value do you want to insert? {}
1. Click on the arrow below
2. Type an integer value [ no comma, no dot, no special characters, only numbers ]
-> """.format('=' * row, '=' * row)

ask_desired_integer = """
{} What is the desired value that you want to find in the range? {}
1. Click on the arrow below
2. Type an integer value [ no comma, no dot, no special characters, only numbers ]
-> """.format('=' * row, '=' * row)

error_not_number = """
{}{} Error found {}{} 
What you typed cannot be determined as an integer value
{}Reminder:{} [ no comma, no dot, no special character, only numbers ]""".format(
    '=' * row, colors['crimson'], colors['standard'], '=' * row, colors['crimson'], colors['standard'])

randomize_creation = []

randomize_precedure = []

randomizer_report = "\nThe number you desire [ {} ] has been found at the index number [ {} ]"

error_inappropriate_value = """
{}{} Error found {}{}
{}Reminder{}: The 2nd integer must be bigger in value than the 1st integer""".format(
    '=' * row, colors['crimson'], colors['standard'], '=' * row, colors['crimson'], colors['standard'])

while True:
    print(welcome)
    algorithm_procedue = input(doubt_run_algorithm)
    if algorithm_procedure in algorithm_cease:
        break
    print(instructions)

    while True:
        try:
            first_integer = int(input(ask_range_first_integer))
            while True:
                try:
                    second_integer = int(input(ask_range_second_integer))
                    if second_integer < first_integer:
                        print(error_inappropriate_value)
                        break
                    while True:
                        try:
                            desired_integer = int(input(ask_desired_integer))
                            randomize_creation = [each_data for each_data in range(first_integer, second_integer)]
                            shuffle(randomize_creation)

                            for each_index, each_data in enumerate(tuple(randomize_creation)):
                                print(each_index, each_data)
                                sleep(0.1)
                                if each_data == desired_integer:
                                    print(randomizer_report.format(
                                                                   desired_integer, each_index))
                                    break
                            break
                        except ValueError:
                            print(error_not_number)
                    break
                except ValueError:
                    print(error_not_number)
            break
        except ValueError:
            print(error_not_number)
"======================================================================================================================"



# Pontilhador de casas numéricas
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_integer

title = '\nWelcome to the {}Integer dot positioner{}'.format(colors['bold_dodgerblue'], colors['standard'])

ask_for_integer = """
{}{} What is the integer to be dotted? {}{}
1. {}
2. Type the integer number
3. {}
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row, click_arrow, press_enter_key)

print(title)

while True:

    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break

    print(title)

    while True:

        try:

            integer = int(input(ask_for_integer))

            if len(str(integer)) == 7:  # 1234567 -> '.' [1]  '.' [5]

                integer_storage = [each_data for each_data in str(integer)]
                integer_storage.insert(1, '.'), integer_storage.insert(5, '.')
                shaped_integer = ''.join(integer_storage)
                print('\n{}{}{}'.format(colors['bold_dodgerblue'], shaped_integer, colors['standard']))

            elif len(str(integer)) == 6:  # 123456 -> '.' [3]

                integer_storage = [each_data for each_data in str(integer)]
                integer_storage.insert(3, '.')
                shaped_integer = ''.join(integer_storage)
                print('\n{}{}{}'.format(colors['bold_dodgerblue'], shaped_integer, colors['standard']))

            elif len(str(integer)) == 5:  # 12345 -> '.' [2]

                integer_storage = [each_data for each_data in str(integer)]
                integer_storage.insert(2, '.')
                shaped_integer = ''.join(integer_storage)
                print('\n{}{}{}'.format(colors['bold_dodgerblue'], shaped_integer, colors['standard']))

            elif len(str(integer)) == 4:  # 12345 -> '.' [1]

                integer_storage = [each_data for each_data in str(integer)]
                integer_storage.insert(1, '.')
                shaped_integer = ''.join(integer_storage)
                print('\n{}{}{}'.format(colors['bold_dodgerblue'], shaped_integer, colors['standard']))

        except ValueError:

            print(mistake_at_integer)
"======================================================================================================================"



# POO: tentativa de algoritmo
"======================================================================================================================"
from resources import *
from datetime import date
from error_handling import (string_incompatible_data,
                            mistake_at_string,
                            improbable_name_size,
                            mistake_at_integer,
                            error_invalid_data)


class Athlete:
    index = 0
    row = 15
    current_year = date.today().year
    data_name = None
    data_birth_year = None
    data_athlete_age = None
    result = []
    name_discard_useless_spacing = None
    name_proper_spacing = None
    name_proper_grammar = None
    shaped_name = None
    senior_age = 30
    professional_age = 18
    junior_age = 14
    infant_age = 10
    invalid_age = 0

    level = ('{}undefined for lack of age{}'.format(colors['bold_dodgerblue'], colors['standard']),
             '{}infant{}'.format(colors['bold_dodgerblue'], colors['standard']),
             '{}junior{}'.format(colors['bold_dodgerblue'], colors['standard']),
             '{}professional{}'.format(colors['bold_dodgerblue'], colors['standard']),
             '{}senior{}'.format(colors['bold_dodgerblue'], colors['standard']))

    instructions = """
{} Instructions {}
1. Provide your name
2. Provide your birth year
3. The algorithm will offer your category based on your age    
""".format('=' * row, '=' * row)

    ask_for_name = """
{} What is your name? {}
1. {}
2. Type your name
3. {}
-> """

    ask_for_birth_year = """
{} What is your birth year? {}
1. {}
2. Type your birth year
3. {}
-> """

    athlete_profile = """
{}{} Athlete profile {}{}
1. Athlete name: {}
2. Athlete birth_year: {}
3. Athlete age: {}
4. Athlete profile level: {}
"""

    @staticmethod
    def name_collect():

        print(Athlete.instructions)
        while True:
            algorithm_action = input(doubt_run_algorithm)
            if algorithm_action in algorithm_cease:
                break
            print(Athlete.instructions)

            Athlete.data_name = input(Athlete.ask_for_name.format('=' * Athlete.row,
                                                                  '=' * Athlete.row,
                                                                  click_arrow,
                                                                  press_enter_key))

            while Athlete.index < len(Athlete.data_name):
                if Athlete.data_name[Athlete.index] in string_incompatible_data:
                    Athlete.result.append(True)
                Athlete.index += 1

            if Athlete.result:
                Athlete.index = 0
                Athlete.result = []
                print(mistake_at_string)
                # break
            else:
                Athlete.name_discard_useless_spacing = Athlete.data_name.split()
                Athlete.name_proper_spacing = ' '.join(Athlete.name_discard_useless_spacing)
                Athlete.name_proper_grammar = Athlete.name_proper_spacing.title()
                Athlete.shaped_name = Athlete.name_proper_grammar
                if len(Athlete.shaped_name) <= 1:
                    print(improbable_name_size)
                else:
                    Athlete.index = 0
                    Athlete.result = []
                    break

    @staticmethod
    def birth_year_collect():

        print(Athlete.instructions)
        while True:
            try:
                Athlete.data_birth_year = int(input(Athlete.ask_for_birth_year.format('=' * Athlete.row,
                                                                                      '=' * Athlete.row,
                                                                                      click_arrow,
                                                                                      press_enter_key)))

                if Athlete.data_birth_year <= 0:
                    print(error_invalid_data)
                else:
                    Athlete.data_athlete_age = Athlete.current_year - Athlete.data_birth_year
                    break

            except ValueError:
                print(mistake_at_integer)

    @staticmethod
    def athlete_profile_report():

        print(Athlete.data_athlete_age)
        if Athlete.data_athlete_age >= Athlete.senior_age:

            print(Athlete.athlete_profile.format('=' * row, colors['bold_dodgerblue'],
                                                 colors['standard'], '=' * row, Athlete.shaped_name,
                                                 Athlete.data_birth_year, Athlete.data_athlete_age,
                                                 Athlete.level[4]))
        elif Athlete.professional_age <= Athlete.data_athlete_age < Athlete.senior_age:

            print(Athlete.athlete_profile.format('=' * row, colors['bold_dodgerblue'],
                                                 colors['standard'], '=' * row, Athlete.shaped_name,
                                                 Athlete.data_birth_year, Athlete.data_athlete_age,
                                                 Athlete.level[3]))
        elif Athlete.junior_age <= Athlete.data_athlete_age < Athlete.professional_age:

            print(Athlete.athlete_profile.format('=' * row, colors['bold_dodgerblue'],
                                                 colors['standard'], '=' * row, Athlete.shaped_name,
                                                 Athlete.data_birth_year, Athlete.data_athlete_age,
                                                 Athlete.level[2]))
        elif Athlete.infant_age <= Athlete.data_athlete_age < Athlete.junior_age:

            print(Athlete.athlete_profile.format('=' * row, colors['bold_dodgerblue'],
                                                 colors['standard'], '=' * row, Athlete.shaped_name,
                                                 Athlete.data_birth_year, Athlete.data_athlete_age,
                                                 Athlete.level[1]))
        elif Athlete.data_athlete_age < Athlete.infant_age:

            print(Athlete.athlete_profile.format('=' * row, colors['bold_dodgerblue'],
                                                 colors['standard'], '=' * row, Athlete.shaped_name,
                                                 Athlete.data_birth_year, Athlete.data_athlete_age,
                                                 Athlete.level[0]))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data_name):
        self.__name = data_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, data_age):
        self.__age = data_age

    def __init__(self, name, age):
        self.__name = name
        self.__age = age


Athlete.name_collect()
Athlete.birth_year_collect()
Athlete.athlete_profile_report()
athlete1 = Athlete(Athlete.shaped_name, Athlete.data_athlete_age)
print('Nome coletado:', athlete1.name)
athlete1.name = 'Alfredo'
print('Nome modificado:', athlete1.name)
print('Idade coletada', athlete1.age)
athlete1.age = 30
print('Idade modificada', athlete1.age)
"======================================================================================================================"



# Protótipo: loja para compras online
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_float, error_invalid_data

input_algorithm_procedure = None
input_expected_value_spent = None
input_chosen_menu_option = None
input_installment_number = None

percentage = 0.15

shopping_cost_with_discount = None
shopping_cost_with_raise = None
price_for_installment = None


def welcome():

    aesthetics = (colors['bold_dodgerblue'], colors['standard'])

    text = '\nWelcome to the {}Prototype of store online purchase{}'

    return text.format(*aesthetics)


def instructions():

    aesthetics = (row, colors['bold_yellowgreen'], colors['standard'], row)

    text = """
{}{} Instructions {}{}
1. Provide how much you expect to spend shopping
2. One menu with four options will pop up
3. Depending on your payment choice, you will have discount or raise in your shopping value
"""
    return text.format(*aesthetics)


def algorithm_start():

    global input_algorithm_procedure

    input_algorithm_procedure = input(doubt_run_algorithm)

    return input_algorithm_procedure


def expected_currency_spent():

    global input_expected_value_spent

    aesthetics = (row, colors['bold_goldenrod'], colors['standard'], row, click_arrow, press_enter_key)

    text = """
{}{} How much currency do you intend to spend shopping? {}{}
1. {}
2. Type the currency amount
3. {}
""".format(*aesthetics)

    input_expected_value_spent = float(input(text))

    return input_expected_value_spent


def menu_options():

    aesthetics = (row, colors['bold_dark_cyan'], colors['standard'], row)

    text = """
{}{} Menu options {}{}
Type one of the options below
[ 1 ] for payment choice in cash (paper money or cheque)
[ 2 ] for payment chocie in cash (credit card)
"""

    return text.format(*aesthetics)


def chosen_menu_option():

    global input_chosen_menu_option

    aesthetics = (row, colors['bold_goldenrod'], colors['standard'], row, click_arrow, press_enter_key)

    text = """
{}{} Which one of the options above do you select? {}{}
1. {}
2. Type one of the options of the menu
3. {}
-> """

    input_chosen_menu_option = int(input(text.format(*aesthetics)))

    return input_chosen_menu_option


def menu_option_one():

    global shopping_cost_with_discount

    shopping_cost_with_discount = input_expected_value_spent - (input_expected_value_spent * percentage)

    aesthetics = (row, row, input_expected_value_spent, shopping_cost_with_discount)

    text = """
{} Discount report {}
You have got a discount percentage for not choosing credit card payment choice
Discount = from [ {:.2f} dollars ] to [ {:.2f} dollars ] 
"""
    return text.format(*aesthetics)


def installment_number():

    global input_installment_number

    aesthetics = (row, colors['bold_goldenrod'], colors['standard'], row, click_arrow, press_enter_key)

    text = """
{}{} What is the number of installments to be split? {}{}
1. {}
2. Type the integer number of installments
3. {}
-> """

    input_installment_number = int(input(text.format(*aesthetics)))

    return input_installment_number


def shopping_report():

    global shopping_cost_with_raise, price_for_installment

    shopping_cost_with_raise = input_expected_value_spent + (input_expected_value_spent * percentage)

    price_for_installment = shopping_cost_with_raise / input_installment_number

    aesthetics = (row, colors['bold_dodgerblue'], colors['standard'], row, input_expected_value_spent,
                  shopping_cost_with_raise, input_installment_number, price_for_installment)

    text = """
{}{} Shopping report {}{}
1. Price raise for choosing credit card: from [ {} dollars ] to [ {} dollars ]
2. Number of installments chosen: [ {} installments ]
3. Price for each installments: [ {:.2f} dollars ]
"""
    return text.format(*aesthetics)


print(welcome())
print(instructions())

while True:
    algorithm_start()
    if input_algorithm_procedure in algorithm_cease:
        break
    while True:
        try:
            expected_currency_spent()
            while input_expected_value_spent <= 0:
                print(error_invalid_data)
                print(instructions())
                expected_currency_spent()
            else:
                break
        except ValueError:
            print(mistake_at_float)
    while True:
        try:
            print(menu_options())
            chosen_menu_option()
            while input_chosen_menu_option <= 0 or input_chosen_menu_option >= 3:
                print(error_invalid_data)
                print(menu_options())
                chosen_menu_option()
            else:
                if input_chosen_menu_option == 1:
                    print(menu_option_one())
                    break
                elif input_chosen_menu_option == 2:
                    while True:
                        try:
                            installment_number()
                            while input_installment_number <= 0:
                                print(error_invalid_data)
                                print(menu_options())
                                installment_number()
                            else:
                                print(shopping_report())
                                break
                        except ValueError:
                            print(mistake_at_float)
            break
        except ValueError:
            print(mistake_at_float)
"======================================================================================================================"



# Protótipo: relógio em tempo real
"======================================================================================================================"
# from datetime import datetime
# from time import sleep
#
# hour = datetime.today().hour
# minute = datetime.today().minute
# second = datetime.today().second
# # list = []
# while True:
#     # list.append('{}h:{}min:{}s'.format(hour, minute, second))
#     # print(list)
#     # list.clear()
#     print('{}h:{}min:{}s'.format(hour, minute, second))
#     second += 1
#     sleep(1)
#     if second == 60:
#         second = 0
#         minute += 1
#         if minute == 60:
#             minute = 0
#             hour += 1
#             if hour == 24:
#                 hour = 0
#                 hour += 1
"======================================================================================================================"



# Radar de trânsito
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_float

title = '\nWelcome to the {}Traffic Scanner{}'.format(colors['dodgerblue'], colors['standard'])

instructions = """
1. Type the speed registered in the report in order to check if it is passive of a traffic ticket
2. The average speed allowed at most 70 kilometers
3. Traspassing it will result in a charge of 7 U$ dollars per kilometer excceeded\n"""

ask_for_velocity = \
"""{} How much speed is the speed report? {}
1. Click on the arrow below
2. Type the speed rate in the report
3. Hit ENTER
-> """.format('=' * row, '=' * row)

no_penalty = "\nYou are fine, keep on this way :D\n"

penalty = None
value_per_exceeded_km = 7
speed_limit_without_punishment = 70
overage = None

penalty_report = """
1. Tolerated speed rate is: [ {}km ]
2. Exceeded by: [ +{:.2f}km(s) ]
3. Speed penalty: [ U$ {:.2f} dollars ]"""

print(title)
while True:
    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break
    print(title)
    print(instructions)
    while True:
        try:
            velocity = float(input(ask_for_velocity))
            if velocity > 70:
                overage = velocity - speed_limit_without_punishment
                penalty = (velocity - speed_limit_without_punishment) * value_per_exceeded_km
                print(penalty_report.format(speed_limit_without_punishment, overage, penalty))
                break
            else:
                print(no_penalty)
                break
        except ValueError:
            print(mistake_at_float, '\n')
"======================================================================================================================"



# Rastreador de caracteres
"======================================================================================================================"
from resources import *
from ansi_colors import *

title = '\nWelcome to the {}Character tracer{}'.format(colors['bold_dodgerblue'], colors['standard'])

space_bar = 'space bar'

instructions = """
1. Provide some text that where a character will be traced
2. Provide the character to be traced
3. The algorithm will provide a report
"""

ask_for_text = """
{}{} What is the target text? {}{}
1. Click on the arrow below
2. Type/copy the target text to be scanned
3. Press ENTER 
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

ask_for_character = """
{}{} What is the [ single ] target character? {}{}
1. Click on the arrow below
2. Type/copy the target character to be found
3. Press ENTER 
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

text_length_allowed = 2

character_length_allowed = 1

trace_report = """
{}{} Report {}{}
1. chosen character: [ {}{}{} ]
2. number of repetitions [ {}{}{} ]
3. 1st occurrence at [ {}index {}{} ]
4. last occurrence at [ {}index {}{} ]"""

error_short_text_input = """
{}{} Error found {}{}
{}The number of character is too short or null. Try again!{}""".format('=' * row,
                                                                       colors['bold_crimson'],
                                                                       colors['standard'],
                                                                       '=' * row,
                                                                       colors['crimson'],
                                                                       colors['standard'])

error_exceeded_number_characters = """
{}{} Error found {}{}
{}Only one ( 1 ) character is allowed!{}""".format('=' * row,
                                                   colors['bold_crimson'],
                                                   colors['standard'],
                                                   '=' * row,
                                                   colors['crimson'],
                                                   colors['standard'])

no_occurrences = """
{}{} No occurrences {}{}
{}The text [ {} ] does not contain the character [ {} ]{}
"""

print(title)

while True:

    algorith_action = input(doubt_run_algorithm)

    if algorith_action in algorithm_cease:
        break  # ceases algotihm

    print(title)

    while True:

        text = input(ask_for_text)

        if len(text) < text_length_allowed:  # if lenght of the text is equals 1 or less

            print(error_short_text_input)

        else:  # continue the algorithm

            while True:

                character = input(ask_for_character)

                if len(character) == character_length_allowed and character in text:

                    print(trace_report.format('=' * row, colors['bold_dodgerblue'], colors['standard'], '=' * row,
                                              colors['bold_dodgerblue'], character, colors['standard'],
                                              colors['bold_dodgerblue'], text.count(character), colors['standard'],
                                              colors['bold_dodgerblue'], text.find(character) + 1, colors['standard'],
                                              colors['bold_dodgerblue'], text.rfind(character) + 1, colors['standard']))
                    break  # exit to algorithm start

                elif len(character) == character_length_allowed and character == ' ':

                    print(trace_report.format('=' * row, colors['bold_dodgerblue'], colors['standard'], '=' * row,
                                              colors['bold_dodgerblue'], space_bar, colors['standard'],
                                              colors['bold_dodgerblue'], text.count(character), colors['standard'],
                                              colors['bold_dodgerblue'], text.find(character) + 1, colors['standard'],
                                              colors['bold_dodgerblue'], text.rfind(character) + 1, colors['standard']))
                    break  # exit to algorithm start

                elif len(character) > character_length_allowed:

                    print(error_exceeded_number_characters)


                elif len(character) == character_length_allowed and character not in text:

                    print(no_occurrences.format('=' * row, colors['bold_crimson'], colors['standard'], '=' * row,
                                                colors['crimson'], text, character, colors['standard']))
                    break  # exit to algorithm start

            break  # exit to algorithm start
"======================================================================================================================"



# Reajuste salarial
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import string_incompatible_data, mistake_at_float

title = '\nWelcome to the {}Salary management{}'.format(colors['bold_dodgerblue'], colors['standard'])

ask_for_name = """
{}{} What is your name? {}{}
1. Click on the arrow below
2. Type your name
3. Press ENTER
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

invalid_data_for_name = """
{}{} Invalid data found {}{}
{}Your name does not contain only letters. Try again!{}""".format('=' * row, colors['bold_crimson'], colors['standard'],
                                                                  '=' * row, colors['crimson'], colors['standard'])
shaped_name = None

judge = []

index = 0


def name_shaper(data_name):

    global shaped_name

    name_discard_useless_spacing = data_name.split()

    name_proper_spacing = ' '.join(name_discard_useless_spacing)

    name_proper_grammar = '{}{}{}'.format(colors['bold_dodgerblue'], name_proper_spacing.title(), colors['standard'])

    shaped_name = name_proper_grammar

display_adjustment_percentage = '\nThe current salary adjustment is [ {}15%{} ]\n'.format(colors['dodgerblue'],
                                                                                          colors['standard'])
ask_for_salary = """
{}{} What is your current salary? {}{}
1. Click on the arrow below
2. Type your salary
3. Press ENTER
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

salary_upgrade_amount_result = []

salary_upgrade_total_result = []

salary_upgrade_report = """
{}{} Salary upgrade report {}{}
Current salary: {}{:.2f}{}
Salary upgraded: {}{:.2f}{}
Upgrade amount: {}+ {:.2f}{}\n"""


def salary_upgrade(data_salary):

    percentage_fifteen = 0.15

    salary_upgrade_amount = data_salary * percentage_fifteen

    salary_upgrade_amount_result.append(salary_upgrade_amount)

    salary_upgrade_total = data_salary + salary_upgrade_amount

    salary_upgrade_total_result.append(salary_upgrade_total)

print(title)

while True:

    algorithm_action = input(doubt_run_algorithm)

    if algorithm_action in algorithm_cease:

        break

    print(title)

    while True:

        employee_name = input(ask_for_name)

        while index < len(employee_name):

            if employee_name[index] in string_incompatible_data:

                judge.append(True)

            index += 1

        while True:

            if True in judge:

                print(invalid_data_for_name)

                judge.clear()

                index = 0

                break

            else:

                judge.clear()

                index = 0

                name_shaper(employee_name)

                print('\nWelcome, {}\n'.format(shaped_name))

                while True:

                    print(display_adjustment_percentage)

                    try:

                        current_salary = float(input(ask_for_salary))

                        salary_upgrade(current_salary)

                        print(salary_upgrade_report.format('=' * row, colors['bold_dodgerblue'], colors['standard'],
                                                           '=' * row, colors['bold_crimson'], current_salary,
                                                           colors['standard'], colors['bold_dodgerblue'],
                                                           salary_upgrade_total_result[0], colors['standard'],
                                                           colors['bold_yellowgreen'], salary_upgrade_amount_result[0],
                                                           colors['standard']))
                        break

                    except ValueError:

                        print(mistake_at_float)

                break

        break
"======================================================================================================================"



# Retornador de divisíveis específicos
"======================================================================================================================"
from resources import *
from error_handling import mistake_at_integer

title = '\nWelcome to the {}untitled{}'.format(colors['bold_dodgerblue'], colors['standard'])

instructions = """
Instructions:\n
1. Inform an {}initial integer{}  [ starting point of the range ] 
2. Inform an {}ultimate integer{} [ ending point of the range   ]
3. Inform an {}divider integer{}  [ divider of the range        ]
4. With the range set, the algorithm will {}return all divisible values by the divider integer{}
5. {}Calculus{} will prove the veracity of the procedure
6. At the end, it will be returned the {}amount of divisible numbers{}""".format(
    colors['dodgerblue'], colors['standard'], colors['dodgerblue'], colors['standard'],
    colors['dodgerblue'], colors['standard'], colors['dodgerblue'], colors['standard'],
    colors['dodgerblue'], colors['standard'], colors['dodgerblue'], colors['standard'],
    colors['dodgerblue'], colors['standard'])

algorithm_sample_demonstration = "\nHit ENTER key to show the sample of the algorithm..."

sample = """
"===================================================="
 [ initial integer ] = 1
 [ ultimate integer ] = 10
 [ divider integer ] = 3

 Chosen range: [ 1 to 10 ]                             
 From          [ 1 to 10 ] values divisible by 3 are: 

 number 3:     [ 3 / 3 = 1 ] [ calculus to prove ]
 number 6:     [ 6 / 3 = 2 ] [ calculus to prove ]
 number 9:     [ 9 / 3 = 3 ] [ calculus to prove ]
"===================================================="
"""

ask_for_initial_integer = """
{}{} What is the initial integer? {}{}
1. Click on the arrow below
2. Type an ultimate integer
3. Press ENTER 
-> """.format(
    '=' * row,
    colors['bold_white'],
    colors['standard'],
    '=' * row)

ask_for_ultimate_integer = """
{}{} What is the ultimate integer? {}{}
1. Click on the arrow below
2. Type an ultimate integer
3. Press ENTER 
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

ask_for_divider_integer = """
{}{} What is the divider integer? {}{}
1. Click on the arrow below
2. Type an ultimate integer
3. Press ENTER 
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

procedure = "\nChosen range: [ {} to {} ]\nFrom          [ {} to {} ] divisible values by [ {} ] are:\n"
procedure_report = "Number {}   [ {} / {} ] = {}"
divisibles_amount = 0
number_divisible_found = "\nOverall number of divibles by [ {} ] found: [ {} numbers ]\n"

print(title)
while True:
    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break

    print(instructions)
    interval = input(algorithm_sample_demonstration)
    print(sample)

    """
    Padrões perceptíveis:
    -> Esqueleto em formato de seta
    -> while True aninhados ficam nivelados e abaixo das vars com inputs
    -> break com 1 identação a frente de except
    """
    while True:
        try:
            initial_integer = int(input(ask_for_initial_integer))
            while True:
                try:
                    ultimate_integer = int(input(ask_for_ultimate_integer))
                    while True:
                        try:
                            divider_integer = int(input(ask_for_divider_integer))

                            print(procedure.format(
                                initial_integer, ultimate_integer,
                                initial_integer, ultimate_integer, divider_integer))

                            for each_data in range(initial_integer, ultimate_integer):
                                if not each_data % divider_integer:
                                    print(procedure_report.format(
                                        each_data, each_data, divider_integer,
                                        each_data / divider_integer))
                                    divisibles_amount += 1

                            print(number_divisible_found.format(divider_integer, divisibles_amount))
                            break
                        except ValueError:
                            print(mistake_at_integer)
                    break
                except ValueError:
                    print(mistake_at_integer)
            break
        except ValueError:
            print(mistake_at_integer)
"======================================================================================================================"



# Retornador de maior e menor número
"======================================================================================================================"
from resources import *
from ansi_colors import colors
from error_handling import mistake_at_float

title = "\nWelcome to the {}Smaller & Bigger number returner{}".format(colors['dodgerblue'], colors['standard'])

instructions = """
1. The algorithm will ask for numbers to add, integers or non-integers, one by one
2. As you add numbers, the algorithm will update the smaller and bigger so far
3. In order to see the final result, type '0'"""

ask_for_number = """
{}{} What number do you want to add? {}{}
1. Click on the arrow below
2. Type an integer or non-integer number
3. Press ENTER
4. Reminder: type 0 if you no longer wish to add data
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

smallest_biggest_report = """\nSmaller value added: [ {}{}{} ]\nBigger value added: [ {}{}{} ]"""
numbers_storage = []
end = [0]
scroll = '\nHit {}ENTER{} to scroll down to the next content\n'.format(colors['dodgerblue'], colors['standard'])

print(title)
while True:
    algorithm_action = input(doubt_run_algorithm)
    if algorithm_action in algorithm_cease:
        break
    print(title)
    while True:
        try:
            print(instructions)
            interval = input(scroll)
            number = float(input(ask_for_number))
            numbers_storage.append(number)  # entradas adicionadas à uma lista externa vazia
            numbers_storage.sort()          # entradas que foram adicionadas à lista vazia, sendo organizadas < >

            if number in end:
                numbers_storage.pop(numbers_storage.index(0))  # remoção da entrada que cessa o loop da lista
                print(smallest_biggest_report.format(colors['dodgerblue'], numbers_storage[0], colors['standard'],
                                                     colors['mediumpurple'], numbers_storage[len(numbers_storage) - 1],
                                                     colors['standard']))
                interval = input(scroll)
                break

            else:
                print(smallest_biggest_report.format(colors['dodgerblue'], numbers_storage[0], colors['standard'],
                                                     colors['mediumpurple'], numbers_storage[len(numbers_storage) - 1],
                                                     colors['standard']))
                interval = input(scroll)
        except ValueError:
            print(mistake_at_float)
"======================================================================================================================"



# Separador de casas decimais
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import mistake_at_integer

title = '\nWelcome to the {}Decimal case splitter{}'.format(colors['bold_dodgerblue'], colors['standard'])

instructions = """
{}{} Instructions {}{}
1. Type an integer number
2. The algorithm will separate each number to its apropriate decimal case
3. A report will be printed to inform the data split result""".format('=' * row, colors['bold_dodgerblue'],
                                                                      colors['standard'], '=' * row)

ask_for_integer = """
{}{} What is the integer to be checked? {}{}
1. {}
2. Type the integer number
3. {}
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row, click_arrow, press_enter_key)

integer_storage = []

shaped_integer = None

decimal_place = [0]


def decimal_place_calculus(data_integer):

    decimal_place.append(int(data_integer) // 1 % 10)
    decimal_place.append(int(data_integer) // 10 % 10)
    decimal_place.append(int(data_integer) // 100 % 10)
    decimal_place.append(int(data_integer) // 1000 % 10)
    decimal_place.append(int(data_integer) // 10_000 % 10)
    decimal_place.append(int(data_integer) // 100_000 % 10)
    decimal_place.append(int(data_integer) // 1_000_000 % 10)

report = """
{}{} Decimal cases found: [ {} ] {}{}
millions =          [ {} ]
hundred thousands = [ {} ]
ten thousands =     [ {} ]
thousands =         [ {} ]
hundreds =          [ {} ]
tens =              [ {} ]
ones =              [ {} ]\n"""

void = '{}no trace!{}'.format(colors['bold_crimson'], colors['standard'])

print(title)

while True:

    algorithm_action = input(doubt_run_algorithm)

    if algorithm_action in algorithm_cease:

        break

    print(title)

    while True:

        try:

            print(instructions)

            integer = int(input(ask_for_integer))

            decimal_place_calculus(integer)

            integer = str(integer)

            if len(integer) == 1:

                print(report.format('=' * row, colors['bold_dodgerblue'], len(integer), colors['standard'],
                                    '=' * row, void, void, void, void, void, void, decimal_place[1]))

                decimal_place.clear()
                decimal_place.append(0)
                break

            elif len(integer) == 2:

                print(report.format('=' * row, colors['bold_dodgerblue'], len(integer), colors['standard'],
                                    '=' * row, void, void, void, void, void, decimal_place[2], decimal_place[1]))

                decimal_place.clear()
                decimal_place.append(0)
                break

            elif len(integer) == 3:

                print(report.format('=' * row, colors['bold_dodgerblue'], len(integer), colors['standard'],
                                    '=' * row, void, void, void, void, decimal_place[3], decimal_place[2],
                                    decimal_place[1]))

                decimal_place.clear()
                decimal_place.append(0)
                break

            elif len(integer) == 4:

                print(report.format('=' * row, colors['bold_dodgerblue'], len(integer), colors['standard'],
                                    '=' * row, void, void, void, decimal_place[4], decimal_place[3], decimal_place[2],
                                    decimal_place[1]))

                decimal_place.clear()
                decimal_place.append(0)
                break

            elif len(integer) == 5:

                print(report.format('=' * row, colors['bold_dodgerblue'], len(integer), colors['standard'],
                                    '=' * row, void, void, decimal_place[5], decimal_place[4], decimal_place[3],
                                    decimal_place[2], decimal_place[1]))

                decimal_place.clear()
                decimal_place.append(0)
                break

            elif len(integer) == 6:

                print(report.format('=' * row, colors['bold_dodgerblue'], len(integer), colors['standard'],
                                    '=' * row, void, decimal_place[6], decimal_place[5], decimal_place[4],
                                    decimal_place[3], decimal_place[2], decimal_place[1]))

                decimal_place.clear()
                decimal_place.append(0)
                break

            elif len(integer) == 7:

                print(report.format('=' * row, colors['bold_dodgerblue'], len(integer), colors['standard'],
                                    '=' * row, decimal_place[7], decimal_place[6], decimal_place[5], decimal_place[4],
                                    decimal_place[3], decimal_place[2], decimal_place[1]))

                decimal_place.clear()
                decimal_place.append(0)
                break

        except ValueError:

            print(mistake_at_integer)
"======================================================================================================================"



# Sistema de aluguel da carros
"======================================================================================================================"
from resources import *
from ansi_colors import *
from error_handling import (mistake_at_float, mistake_at_integer)

title = '\nWelcome to the{} Car renting system{}'.format(colors['bold_dodgerblue'], colors['standard'])

ask_number_rent_days = """
{}{} For how many days have you rented the vehicle? {}{}
1. Click on the arrow below
2. Type the number of days
3. Hit ENTER
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

ask_number_traveled_kilometers = """
{}{} For how many kilometers has the vehicle traveled? {}{}
1. Click on the arrow below
2. Type the number of kilometers
3. Hit ENTER
-> """.format('=' * row, colors['bold_white'], colors['standard'], '=' * row)

daily_use_charge = 60
charge_per_kilometer = 0.15


def price_to_pay():
    global charge_per_kilometer, daily_use_charge, rent_days, traveled_kilometers

    print(
"""
{}Report{}
Number of days owning the vehicle     = [ {} days ]
Kilometers traveled with the vehicle  = [ {} kilometers ]
Price to pay in U$                    = [ {:.2f} ]""".format(
                                                             colors['bold_dodgerblue'],
                                                             colors['standard'],
                                                             rent_days,
                                                             traveled_kilometers,
                                                            (daily_use_charge * rent_days) +
                                                            (charge_per_kilometer * traveled_kilometers)))

while True:
    algorith_action = input(doubt_run_algorithm)
    if algorith_action in algorithm_cease:
        break
    print(title)
    while True:
        try:
            rent_days = int(input(ask_number_rent_days))
            while True:
                try:
                    traveled_kilometers = float(input(ask_number_traveled_kilometers))
                    price_to_pay()
                    break
                except ValueError:
                    print(mistake_at_float)
            break
        except ValueError:
            print(mistake_at_integer)
"======================================================================================================================"
