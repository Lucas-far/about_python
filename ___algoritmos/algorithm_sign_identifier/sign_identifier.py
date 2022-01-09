

from methods_database import (
    calculate_lifetime,
    customize_birthday,
    find_sign,
    get_input_integer,
    instructions,
    should_algorithm_run,
    welcome
)

from widgets import (
    the_breaking_point,
    the_closure
)

from algorithm_sign_identifier.string_database import *

steps: tuple = ('',
                '1 - Should algorithm run?',
                '2 - Display of instructions',
                '3 - Provide input: birth day',
                '4 - Provide input: birth month',
                '5 - Provide input: birth year',
                '6 - Display of result')

steps: tuple = tuple([f'\n{colors[2]}{step}{colors[-1]}\n' for step in steps])

input_exec: str = ''
input_birth_day: int = 1
input_birth_month: int = 1
input_birth_year: int = 1

user_birthday = None
user_birthday_str: str = ''
user_lifetime: str = ''


def start():
    """"""
    global input_exec
    print(steps[1])
    input_exec = input(should_algorithm_run())


while True:

    welcome('Sign Identifier')
    start()

    if input_exec in the_breaking_point:
        print(the_closure)
        break

    instructions(the_content=f"""
                 {steps[2]}
                 {text_instructions}""")

    input_birth_day = get_input_integer(the_input=input_birth_day,
                                        input_text=f"""
                                        {steps[3]}
                                        {text_ask_birth_day}""",
                                        the_initial_integer=1,
                                        the_last_integer=31)

    input_birth_month = get_input_integer(the_input=input_birth_month,
                                          input_text=f"""
                                          {steps[4]}
                                          {text_ask_birth_month}""",
                                          the_initial_integer=1,
                                          the_last_integer=12)

    input_birth_year = get_input_integer(the_input=input_birth_year,
                                         input_text=f"""
                                         {steps[5]}
                                         {text_ask_birth_year}""",
                                         the_initial_integer=1,
                                         the_last_integer=9_999)

    user_birthday, user_birthday_str = customize_birthday(the_birthday=user_birthday,
                                                          the_birthday_srt=user_birthday_str,
                                                          year=input_birth_year,
                                                          month=input_birth_month,
                                                          day=input_birth_day)

    user_lifetime = calculate_lifetime(birthday=user_birthday,
                                       the_result=user_lifetime)

    the_report = find_sign(birthday=user_birthday_str,
                           existence=user_lifetime,
                           day=input_birth_day,
                           month=input_birth_month)

    # print([1], input_birth_day)
    # print([2], input_birth_month)
    # print([3], input_birth_year)
    # print([4], user_birthday)
    # print([5], user_birthday_str)
    # print([6], user_lifetime)
    print(the_report)
