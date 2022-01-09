

def mtd_calculate_lifetime(birthday):
    """
    To calculate user's lifetime by subtracting the day represeting today by someone's birthday

    :param birthday: must be a datetime object [ex] var = datetime(year=int, month=int, day=int)
    :return: the string which reports the result of the calculus
    """

    from datetime import datetime

    today = datetime.today()
    the_existence_calculus = today - birthday
    the_result = f'Você têm por volta de {str(the_existence_calculus).split()[0]} dias vividos'

    # ---------------------------------------------------- EXAMPLE ----------------------------------------------------
    # the_existence_calculus = 2020/07/08 - 1992/7/16 = 10219 days, 23:33:12.115426
    # the_result = About 10219 days

    return the_result


class MtdCalculateLifetime:

    from datetime import datetime

    today = datetime.now()

    @staticmethod
    def show_my_age_in_days(date_data) -> str:
        my_age = f'Você têm por volta de {str(date_data).split()[0]} dias vividos'
        return my_age

    @property
    def return_birthday(self) -> datetime:
        return self.__birthday

    @return_birthday.setter
    def return_birthday(self, new_value):
        self.__birthday = new_value

    def __init__(self, birthday: datetime):
        self.__birthday = birthday

    def calculate_existence(self):
        the_existence_calculus = MtdCalculateLifetime.today - self.__birthday
        return the_existence_calculus


if __name__ == '__main__':

    from datetime import datetime

    structured = '------------------------------------- PROGRAMAÇÃO ESTRUTURAL -------------------------------------\n'
    oriented = '---------------------------------- PROGRAMAÇÃO ORIENTADA A OBJETOS ----------------------------------\n'

    # --------------------------------------------- PROGRAMAÇÃO ESTRUTURAL ---------------------------------------------
    argument = datetime(year=1953, month=6, day=1)  # argumento
    object_main = mtd_calculate_lifetime(birthday=argument)
    print(f'{structured}{object_main}')

    # ---------------------------------------- PROGRAMAÇÃO ORIENTADA A OBJETOS ----------------------------------------
    an_object = MtdCalculateLifetime(birthday=argument)
    object_days_alive = an_object.calculate_existence()
    object_days_alive_str = an_object.show_my_age_in_days(date_data=object_days_alive)
    print(f'{oriented}{object_days_alive_str}')
