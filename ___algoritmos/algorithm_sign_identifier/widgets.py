

colors: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
)

# -------------------------------------------------- Utility strings --------------------------------------------------
algorithm_closure: tuple = ('n',)
the_breaking_point: tuple = ('n',)
scrolling_blocker: str = "Press any key in order to continue..."
click_arrow: str = 'Click after the arrow below'
hit_enter: str = 'Press ENTER key'
the_closure: str = f'{colors[1]}\nAlgorithm has been shut down{colors[-1]}'
instruction = f'\n{colors[2]}Press ENTER to continue{colors[-1]}\n'
# ---------------------------------------------------------------------------------------------------------------------


def error_input_floating_out_of_range(first_value: float = 0.0,
                                      last_value: float = 0.0):

    inks: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    announcement = f"""{inks[1]}
    =============== ERROR ==============={inks[-1]}
    The provided input is not floating in the suitable range: {first_value} to {last_value}"""

    return announcement


def error_input_floating_not_used(first_value: float = 0.0,
                                  last_value: float = 0.0):

    inks: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    announcement = f"""{inks[1]}
    =============== ERROR ==============={inks[-1]}
    The provided input must be a floating number between: {first_value} to {last_value}"""

    return announcement


def error_input_non_integer():

    inks: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    announcement = f"""{inks[1]}
    =============== ERROR ==============={inks[-1]}
    1 - The input provided does not seem to be exactly an integer value
    2 - Please, avoid using integer numbers with {inks[1]}special characters{inks[-1]}"""

    return announcement


def error_input_non_numerical():

    inks: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    announcement = f"""{inks[1]}
    =============== ERROR ==============={inks[-1]}
    1 - The input provided does not seem to be entirely numerical
    
    2 - For integer input: Use underline to separate numbers with 4+ digits
        EXAMPLE: 1_234, 12_345, 123_456, 1_234_567
    
    3 - For non-integer input: Use underline to separate integer fields and dot to separate decimal fields
        EXAMPLE: 1_234.5, 12_345.6, 123_456.7, 1_234_567.8 """

    return announcement


if __name__ == '__main__':

    space = '\n'
    print(error_input_floating_out_of_range(first_value=2.2, last_value=7.7))
    print(space)
    print(error_input_floating_not_used(first_value=2.2, last_value=7.7))
    print(space)
    print(error_input_non_integer())
    print(space)
    print(error_input_non_numerical())
