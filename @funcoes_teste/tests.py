

from unittest import TestCase
from datetime import datetime

from metodos_bdd.calculate_lifetime import mtd_calculate_lifetime
from metodos_bdd.day_suffix_manager import mtd_day_suffix_manager
from metodos_bdd.turn_date_into_str import mtd_turn_date_into_str

# python -m unittest discover methods_test (last syntax is the directory where the test module finds itself in)


class TestMtdCalculateLifetime(TestCase):

    def setUp(self) -> None:
        self.my_birthday = datetime(year=1953, month=6, day=1)
        self.object_for_test = mtd_calculate_lifetime(birthday=self.my_birthday)

    def test_mtd_calculate_lifetime(self):
        self.my_birthday = datetime(year=1953, month=6, day=1)
        self.my_birthday2 = datetime(year=1943, month=7, day=16)
        self.object = mtd_calculate_lifetime(self.my_birthday)
        self.object2 = mtd_calculate_lifetime(self.my_birthday2)
        self.assertEqual(self.object_for_test, self.object)
        self.assertNotEqual(self.object_for_test, self.object2)


class TestMtdDaySuffixManager(TestCase):

    def setUp(self):
        self.object_for_test = mtd_day_suffix_manager(day='1')

    def test_mtd_day_suffix_manager(self):
        self.object = mtd_day_suffix_manager(day='1')
        self.object2 = mtd_day_suffix_manager(day='2')
        self.assertEqual(self.object_for_test, self.object)
        self.assertNotEqual(self.object_for_test, self.object2)


# Ran 1 test in 0.003s OK
class TestMethodTurnDateIntoStr(TestCase):

    def setUp(self) -> None:
        self.object_for_test = mtd_turn_date_into_str(year=1989, month=9, day=20)

    def test_mtd_turn_date_into_str(self):
        self.object = mtd_turn_date_into_str(year=1989, month=9, day=20)
        self.object2 = mtd_turn_date_into_str(year=1990, month=9, day=20)
        self.assertEquals(self.object_for_test, self.object)
        self.assertNotEquals(self.object_for_test, self.object2)


# # Ran 1 test in 0.004s OK
# class TestMethodTurnDateIntoStr(TestCase):
#
#     def setUp(self) -> None:
#         self.var = mtd_turn_date_into_str(1989, 9, 20)
#
#     def test_mtd_turn_date_into_str(self):
#         self.var2 = mtd_turn_date_into_str(1990, 9, 20)
#         self.assertNotEquals(self.var, self.var2)
