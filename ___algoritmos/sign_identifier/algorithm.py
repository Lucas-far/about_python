

class Sign:

    alert_algorithm_title = '\nBEM-VINDO AO IDENTIFICADOR DE SIGNOS\n'
    alert_algorithm_question = 'Should the algorithm run?\n'
    alert_make_algorithm_start = 'Para continuar: aperte "1" ou qualquer outra tecla \n'
    alert_make_algorithm_cease = 'Para sair: aperte "0" \n'

    alert_instructions = '\nINSTRUCTIONS\n'
    alert_day = '1 - Provide the day you were born \n'
    alert_month = '2 - Provide the month you were born \n'
    alert_year = '3 - Provide the year you were born\n'
    alert_algorithm_procedures = "4 - The algorithm will return user's sign and time of existence"

    alert_input_first = '\nProvide input: birth day\n'
    alert_input_first_instruction = 'Digite um valor entre 1 até 31\n'

    alert_input_second = 'Provide input: birth month\n'
    alert_input_second_instruction = 'Digite um valor entre 1 até 12'

    alert_input_third = 'Provide input: birth year\n'
    alert_input_third_instruction = 'Digite um valor entre 1 até 9999'

    alert_result = 'RESULT\n'

    alert_ok = 'Obrigado por informar, vamos ao próximo passo.'
    alert_not_ok = '\nVocê não forneceu o dado esperado.\n'

    alert_where_to_type = 'Por favor, digite após a seta -----> '
    alert_shutdown = 'Algorithm has been shut.'

    @staticmethod
    def ink(text: str):
        """"""

        from random import choice

        inks: tuple = (
            '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m',
            '\033[1:37m', '\033[1:38m',
        )

        return f"{choice(inks)}{text}{inks[-1]}"

    @staticmethod
    def skip_line(text):
        return '\n' + text

    @staticmethod
    def indented(text):
        return '    ' + text

    @staticmethod
    def launch_algorithm(text_instruction, breaker, text_closure):

        launcher = input(text_instruction)
        for data in breaker:
            if launcher == data:
                print(Sign.ink(text=text_closure))
                return True
        return None

    @staticmethod
    def get_input(text_instruction, integer_based, from_integer, to_integer, message_success, message_error):

        while True:
            if integer_based:
                box = tuple(range(from_integer, to_integer + 1))
                box_str = tuple(str(number) for number in box)

                this_input = input(text_instruction)
                if this_input in box_str:
                    print(message_success)
                    return this_input
                else:
                    print(message_error)

    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year


if __name__ == '__main__':

    message_welcome = Sign.ink(Sign.alert_algorithm_title)

    guide = (
        Sign.alert_algorithm_question,
        Sign.alert_make_algorithm_start,
        Sign.alert_make_algorithm_cease,
        Sign.alert_where_to_type
    )

    guide2 = (
        Sign.ink(Sign.alert_instructions),
        Sign.alert_day,
        Sign.alert_month,
        Sign.alert_year,
        Sign.alert_algorithm_procedures,
    )

    guide3 = (
        Sign.ink(Sign.alert_input_first),
        Sign.alert_input_first_instruction,
        Sign.alert_where_to_type
    )

    while True:
        print(message_welcome)

        decision = Sign.launch_algorithm(text_instruction=guide[0] + guide[1] + guide[2] + guide[3],
                                         breaker=('0',),
                                         text_closure=Sign.ink(Sign.alert_shutdown))

        if decision:
            break
        print(guide2[0] + guide2[1] + guide2[2] + guide2[3] + guide2[4])

        the_day = Sign.get_input(text_instruction=guide3[0] + guide3[1] + guide3[2],
                                 integer_based=True,
                                 from_integer=1,
                                 to_integer=31,
                                 message_success=Sign.ink(Sign.alert_ok),
                                 message_error=Sign.ink(Sign.alert_not_ok))

        print(the_day)
