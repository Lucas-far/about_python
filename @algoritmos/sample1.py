

""""""

from datetime import datetime
from time import sleep
from methods_database import (
    integer_out_of_range, integer_unused
)
from widgets import (
    click_arrow, closure, colors, hit_enter, scrolling_blocker, should_algorithm_run, the_breaking_point, welcome
)

input_exec: str = ''
input_birth_day: int = 1
input_birth_month: int = 1
input_birth_year: int = 1

user_custom_birth = datetime(year=1, month=1, day=1)
user_custom_birth_srt: str = ''
existence_calculus = datetime(year=1, month=1, day=1)
date_today = datetime.today()
user_lifetime: str = ''

# Variables for function: custom_conditions()
each_sign_first_month_days: list = []
each_sign_first_month: tuple = ()
each_sign_second_month_days: list = []
each_sign_second_month: tuple = ()

# Variables for function: throw_result()
index: int = 0
counter: int = 0
result_text: str = ''
signs: tuple = ('Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Saggitarius')
signs: tuple = tuple([f'{colors[4]}{sign}{colors[7]}' for sign in signs])
steps: tuple = ('',
                '1 - Should algorithm run?',
                '2 - Display of instructions',
                '3 - Provide input: birth day',
                '4 - Provide input: birth month',
                '5 - Provide input: birth year',
                '6 - Display of result')
steps: tuple = tuple([f'\n{colors[2]}{step}{colors[7]}\n' for step in steps])

def start():
    """
    To ask if algorithm must or not run. Any key pressed = continue. String 'n' = break.
    """
    global input_exec
    print(steps[1])
    input_exec = input(should_algorithm_run())

def instructions():
    """ To inform procedures of the algorithm. """

    text: str = f"""
    {steps[2]}
    ========== INSTRUCTIONS ==========
    1 - Provide your {colors[1]}birth day{colors[7]}
    2 - Provide your {colors[1]}birth month{colors[7]}
    3 - Provide your {colors[1]}birth year{colors[7]}
    4 - The algorithm will return user's sign and lifetime existence
    """
    print(text)
    input(scrolling_blocker)

def get_birth_day():
    """
    To treat improper data while a proper integer number is not being provided.
    """
    global input_birth_day

    input_text = f"""
    {steps[3]}
    ======= QUESTION: {colors[0]}In what day have you been born?{colors[7]} =======
    1 - {click_arrow}
    2 - Type the day you have been born (from 1 to 31)
    3. {hit_enter}
    -------> """

    while True:
        try:
            input_birth_day = int(input(input_text))
            while input_birth_day <= 0 or input_birth_day > 31:  # while input = improper number
                integer_out_of_range(1, 31)                      # throw this error function
                get_birth_day()                                  # repeat main function
            else:                                                # otherwise
                break                                            # go to the next step
        except ValueError:                                       # except if input = wrong type
            integer_unused(1, 31)                                # then throw this error function, loop repeats

def get_birth_month():
    """
    To treat improper data while a proper integer number is not being provided.
    """
    global input_birth_month

    input_text: str = f"""
    {steps[4]}
    ======= QUESTION: {colors[0]}In what month have been born?{colors[7]} =======
    1. {click_arrow}
    2. Type the month you have been born (from 1 to 12)
    3. {hit_enter}
    -------> """

    while True:
        try:
            input_birth_month = int(input(input_text))
            while input_birth_month < 1 or input_birth_month > 12:  # while input = improper number
                integer_out_of_range(1, 12)                         # throw this error function
                get_birth_month()                                   # repeat main function
            else:                                                   # otherwise
                break                                               # go to the next step
        except ValueError:                                          # except if input = wrong type
            integer_unused(1, 12)                                   # then throw this error function, loop repeats

def get_birth_year():
    """
    To treat improper data while a proper integer number is not being provided.
    """
    global input_birth_year

    input_text: str = f"""
    {steps[5]}
    ======= QUESTION: {colors[0]}In what year have you been born?{colors[7]} =======
    1 - {click_arrow}
    2. Type the year you have been born (from year 1 to 9999)
    3 - {hit_enter}
    -------> """
    max_year = 9999

    while True:
        try:
            input_birth_year = int(input(input_text))
            while input_birth_year <= 0 or input_birth_year > max_year:  # while input = improper number
                integer_out_of_range(1, 9999)                            # throw this error function
                get_birth_year()                                         # repeat main function
            else:                                                        # otherwise
                break                                                    # go to the next step
        except ValueError:                                               # except if input = wrong type
            integer_unused(1, 9999)                                      # then throw this error function, loop repeats

def custom_birth_date(year: int = 1, month: int = 1, day: int = 1):
    """
    To build a datetime variable from a birthday.
    """

    global user_custom_birth, user_custom_birth_srt
    user_custom_birth = datetime(year=year, month=month, day=day)
    user_custom_birth_srt = f'{year}/{month}/{day}'

def calculate_lifetime():
    """
    To calculate user's lifetime.
    """

    global existence_calculus, user_lifetime
    existence_calculus = date_today - user_custom_birth                 # ex: var = 2020/07/08 - 1992/7/17 = 10219 days, 23:33:12.115426
    user_lifetime = f'About {str(existence_calculus).split()[0]} days'  # ex: var = About 10219 days

#
#     user_lifetime = f'{colors[3]}{user_lifetime}{colors[7]}'
#
#     # ========== TUTORIAL ==========
#     # Assumptions:
#     # date_today = 2020/07/08
#     # user_custom_birth = datetime(year=1992, month=7, day=16)
#
#     # existence_calculus = 2020/07/08 - 1992/7/17
#     # existence_calculus = 10219 days, 23:33:12.115426
#
#     # user_lifetime = f'About {str(existence_calculus).split()[0]} days'
#     # user_lifetime = f'About {'10219 days, 23:33:12.115246'.split()[0]} days'
#     # user_lifetime = f'About {['10219' 'days,' '23:33:12.115426'][0]} days'
#     # user_lifetime = f'About 10219 days'
# def procedures_texts():
#     """To display procedures which are being executed."""
#
#     print(f"\n{colors[0]}Getting current date...{colors[7]}"), sleep(0.25)
#     print(f"{colors[0]}Scanning user's month...{colors[7]}"), sleep(0.25)
#     print(f"{colors[0]}Customizing user's date...{colors[7]}"), sleep(0.25)
#     print(f"{colors[0]}Calculating user's day of living...{colors[7]}"), sleep(0.25)
#     print(f"{colors[0]}Building user's day of living...{colors[7]}"), sleep(0.25)
#     print(f"{colors[0]}Finding user's sign...{colors[7]}"), sleep(0.25)
#     print(f"{colors[0]}Ready!{colors[7]}\n")
# def custom_conditions():
#     """To custom conditions for each sign and print the result of the only possibility."""
#
#     global each_sign_first_month_days, each_sign_first_month, each_sign_second_month_days, each_sign_second_month
#
#     each_sign_first_month_days = (
#         range(22, 32),  # days of the first month of Capricorn
#         range(21, 32),  # ...Aquarius
#         range(19, 32),  # ...Pisces
#         range(21, 32),  # ...Aries
#         range(21, 32),  # ...Taurus
#         range(21, 32),  # ...Gemini
#         range(21, 32),  # ...Cancer
#         range(23, 32),  # ...Leo
#         range(23, 32),  # ...Virgo
#         range(23, 32),  # ...Libra
#         range(23, 32),  # ...Scorpio
#         range(22, 32))  # ...Sagittarius
#
#     each_sign_first_month = (12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
#
#     each_sign_second_month_days = (
#         range(1, 21),  # days of the second month of Capricorn
#         range(1, 19),  # ...Aquarius
#         range(1, 21),  # ...Pisces
#         range(1, 21),  # ...Aries
#         range(1, 21),  # ...Taurus
#         range(1, 21),  # ...Gemini
#         range(1, 23),  # ...Cancer
#         range(1, 23),  # ...Leo
#         range(1, 23),  # ...Virgo
#         range(1, 23),  # ...Libra
#         range(1, 22),  # ...Scorpio
#         range(1, 22))  # ...Sagittarius
#
#     each_sign_second_month = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
#
#     # ========== TUTORIAL ==========
#     # each_sign_first_month_days[0] and each_sign_first_month[0]   = Capricorn
#     # each_sign_second_month_days[0] and each_sign_second_month[0] = Capricorn
#
#     # each_sign_first_month_days[1] and each_sign_first_month[1]   = Aquarius
#     # each_sign_second_month_days[1] and each_sign_second_month[1] = Aquarius
#
#     # and so on so forth...
# def throw_result():
#     """To fill a string with collected data"""
#
#     global index, counter, result_text
#
#     result_text = \
#     """
#     {}
#     =====================
#     | Birth             | {}
#     | Sign              | {}
#     | Days of existence | {}
#     =====================
#     """
#
#     # ========== TUTORIAL==========
#     # Variable (index) avoids writing many conditions
#     # It starts as 0, but can be incremented until 12
#     # It controls the going through from each index of the 4 target sign variables below
#     # If it gets two True conditions in a row, it will trigger the result
#
#     while counter < len(signs):  # counter may increment until integer 12, depending on the result
#
#         if input_birth_day in each_sign_first_month_days[index] and input_birth_month == each_sign_first_month[index] \
#         or input_birth_day in each_sign_second_month_days[index] and input_birth_month == each_sign_second_month[index]:
#
#             print(result_text.format(steps_colored[6], user_custom_birth_srt, signs[index], user_lifetime))
#             break
#         else:
#             counter += 1
#             index += 1
#     # variables must be reset at the end
#     counter = 0
#     index = 0

while True:
    welcome('Sign Identifier')
    start()
    if input_exec in the_breaking_point:
        print(closure)
        break
    instructions()
    get_birth_day()
    get_birth_month()
    get_birth_year()
    custom_birth_date(input_birth_year, input_birth_month, input_birth_day)
    calculate_lifetime()
    print(existence_calculus)
    print(user_lifetime)
    # instructions()
    # get_birth_day()
    # get_birth_month()
    # get_birth_year()
    # custom_birth_date(input_birth_year, input_birth_month, input_birth_day)
    # custom_str_birth_date(input_birth_year, input_birth_month, input_birth_day)
    # calculate_lifetime()
    # procedures_texts()
    # custom_conditions()
    # throw_result()
