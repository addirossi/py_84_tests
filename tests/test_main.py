import unittest
from unittest import TestCase

import pytest

from main import summarize, get_dict, multiply


# class TestSummarize(TestCase):
#     def setUp(self):
#         self.a = 10
#         # self.user = User(...)
#         self.list1 = [1, 2, 3, 4]
#
#     def test_2_positive_number(self):
#         a, b = self.a, 20
#         expected = 30
#         result = summarize(a, b)
#         self.assertEqual(result, expected)  #assert result == expected
#
#     def test_negative_failed(self):
#         a = self.a
#         b = -20
#         expected = -5
#         result = summarize(a, b)
#         self.assertEqual(result, expected)
#
#     def test_error(self):
#         a = self.a
#         b = '20'
#         expected = 35
#         result = summarize(a, b)
#         self.assertEqual(result, expected)
#
#
# class TestSomething(TestCase):
#     def test_1(self):
#         a, b = 10, 57
#         expected = 60
#         result = summarize(a, b)
#         self.assertGreater(result, expected)
#
#     def test_2(self):
#         key = 'surname'
#         dict1 = get_dict()
#         # self.assertIn(key, dict1)
#         self.assertNotIn(key, dict1)
#
#     def test_regex(self):
#         date1 = '19.10.2023'
#         format1 = '\d{2}\-\d{2}\-\d{4}'
#         format2 = '\d{2}\.\d{2}.\d{4}'
#         # self.assertRegex(date1, format1)
#         self.assertRegex(date1, format2)
#
#     def test_or(self):
#         a, b = 10, 20
#         expected1 = 15
#         expected2 = 30
#         result = summarize(a, b)
#         self.assertTrue(result == expected1 or result == expected2)
#         self.assertIn(result, [expected1, expected2])


# def test_something():
#     a, b = 10, 20
#     expected = 30
#     result = summarize(a, b)
#     assert result == expected
#
#
# class TestMultiply():
#     def test_1(self):
#         x, y = 29, 20
#         expected = 580
#         result = multiply(x, y)
#         assert result == expected


# class Phone(Model):
#     name = ...
#     description = ...
#     price = ...


# class TestDjango(TestCase):
#     def setUp(self):
#         self.phone1 = Phone(name='Apple Iphone', ...)
#         self.phone2 = Phone(name='Samsung', ...)
#
#     def test_get_list(self):
#         client = APIClient()
#         response = client.get('/products/')
#         assert response.status_code == 200
#         assert len(response.data) == 2
#         assert response.data[0].name == self.phone1.name



from config import NUMBER

# ожидаемое падение тестов
class TestExpectedFailure(TestCase):
    def test_2_positive_number(self):
        a, b = 10, 20
        expected = 30
        result = summarize(a, b)
        self.assertEqual(result, expected)

    @unittest.expectedFailure
    def test_failed(self):
        a, b = 47, 32
        expected = 76
        result = summarize(a, b)
        self.assertEqual(result, expected)

    @unittest.expectedFailure
    def test_error(self):
        a, b = 12, '23'
        expected = 35
        result = summarize(a, b)
        self.assertEqual(result, expected)

    # def test_yandex(self):
    #     token = '....'
    #     path = '...'
    #     fields = '...'
    #     result = get_yandex(path, fields)
    #     self.assertEqual(result.status_code == 200)

    #пропуск теста
    @unittest.skipIf(NUMBER < 50, 'Too low value')
    def test_skipped(self):
        a, b = 10, 20
        expected = 200
        result = multiply(a, b)
        self.assertEqual(result, expected)


@pytest.mark.xfail
def test_failed():
    a, b = 47, 32
    expected = 76
    result = summarize(a, b)
    assert result == expected

# пропуск теста
@pytest.mark.skipif(NUMBER < 50, reason='Too low value')
def test_skipped(self):
    a, b = 10, 20
    expected = 200
    result = multiply(a, b)
    self.assertEqual(result, expected)

#параметризация
@pytest.mark.parametrize(
    "x,y,expected",
    [
        (20, 13, 33),
        (-15, -16, -31),
        (100, 291, 391),
        (76, 24, 100)
    ]
)
def test_with_params(x, y, expected):
    result = summarize(x, y)
    assert result == expected