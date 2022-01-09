

from methods_database import colors

from widgets import (click_arrow, hit_enter)


text_instructions = f"""
    ========== INSTRUCTIONS ==========
    1 - Provide your {colors[1]}birth day{colors[-1]}
    2 - Provide your {colors[1]}birth month{colors[-1]}
    3 - Provide your {colors[1]}birth year{colors[-1]}
    4 - The algorithm will return user's sign and time of existence"""

text_ask_birth_day = f"""
    ======= QUESTION: {colors[0]}In what day have you been born?{colors[-1]} =======
    1 - {click_arrow}
    2 - Type the day you have been born (from 1 to 31)
    3 - {hit_enter}
    -------> """

text_ask_birth_month = f"""
    ======= QUESTION: {colors[0]}In what month have been born?{colors[-1]} =======
    1 - {click_arrow}
    2 - Type the month you have been born (from 1 to 12)
    3 - {hit_enter}
    -------> """

text_ask_birth_year = f"""
    ======= QUESTION: {colors[0]}In what year have you been born?{colors[-1]} =======
    1 - {click_arrow}
    2. Type the year you have been born (from year 1 to 9999)
    3 - {hit_enter}
    -------> """
