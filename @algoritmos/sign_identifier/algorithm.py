

class Sign:

    line = '\n'
    indent = '    '

    alert_algorithm_title = 'BEM-VINDO AO IDENTIFICADOR DE SIGNOS\n'
    alert_algorithm_question = 'Should the algorithm run?\n'
    alert_instructions = 'INSTRUCTIONS\n'
    alert_input_first = 'Provide input: birth day\n'
    alert_input_second = 'Provide input: birth month\n'
    alert_input_third = 'Provide input: birth year\n'
    alert_result = 'RESULT\n'
    alert_make_algorithm_start = 'Para continuar: aperte "1" ou qualquer outra tecla \n'
    alert_make_algorithm_cease = 'Para sair: aperte "0" \n'
    alert_day = '1 - Provide the day you were born \n'
    alert_month = '2 - Provide the month you were born \n'
    alert_year = '3 - Provide the year you were born\n'
    alert_algorithm_procedures = "4 - The algorithm will return user's sign and time of existence"
    alert_for_day_input = 'Digite um valor entre 1 até 31'
    alert_ok = 'Obrigado por informar, vamos ao próximo passo.'
    alert_not_ok = f'Você não forneceu o dado esperado.'
    alert_where_to_type = 'Por favor, digite após a seta -----> '
    alert_shutdown = 'Algorithm has been shut.'

    @staticmethod
    def paint_it_random(text: str):
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
                print(Sign.paint_it_random(text=text_closure))
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

    message_welcome = Sign.alert_algorithm_title
    message_instructions = {Sign.paint_it_random(Sign.show_steps(label='2'))}
    message_instruction2 = Sign.paint_it_random(Sign.show_steps(label='3'))
    message_instruction3 = Sign.paint_it_random(Sign.show_steps(label='4'))

    guide = (Sign.alert_make_algorithm_start,
             Sign.alert_make_algorithm_cease,
             Sign.alert_where_to_type
    )

    while True:
        print(Sign.line)
        print(message_welcome)

        decision = Sign.launch_algorithm(text_instruction=guide[0] + guide[1] + guide[2],
                                         breaker=('0',),
                                         text_closure=Sign.alert_shutdown)

        if decision:
            break
        print(Sign.skip_line(text=Sign.indented(text=message_instruction2)))
        print(Sign.indented(text=Sign.alert_1))
        print(Sign.indented(text=Sign.alert_2))
        print(Sign.indented(text=Sign.alert_3))
        print(Sign.indented(text=Sign.alert_4))

        print(message_instruction3)
        print(Sign.alert_for_day_input)
        day = Sign.get_input(text_instruction=Sign.alert_where_to_type,
                             integer_based=True,
                             from_integer=1,
                             to_integer=31,
                             message_success=Sign.alert_ok,
                             message_error=Sign.alert_not_ok)
