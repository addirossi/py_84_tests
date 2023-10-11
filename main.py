def summarize(x: int, y: int) -> int:
    return x + y


def multiply(x: int, y: int) -> int:
    return x * y


def get_dict():
    return {'name': 'Ivan', 'age': 29, 'city': 'Moscow'}


def get_list():
    return [1, 2, 3, 4]


#1
# a, b = 10, 20
# expected = 30
# result = summarize(a, b)
# assert result == expected

# try:
#     a, b = 29, 35
#     expected = 65
#     result = summarize(a, b)
#     assert result == expected
# except AssertionError:
#     print('Тест не пройден')


# операции сравнения ==, !=, >, <, >=, <=
# is, is not
# in, not in
# isinstance(), issubclass()
