import pytest

from utils.arrs import get


@pytest.mark.parametrize('array, index, expected, default', [
    ([1, 2, 3], 1, 2, "test"),
    ([], 0, "test", "test"),
    ([1, 2, 3], -1, "test", "test")
])

def test_get(array, index, expected, default):
    assert get(array, index, default) == expected
# Функция без фикстур
# def test_get():
#     assert arrs.get([1, 2, 3], 1, "test") == 2
#     assert arrs.get([], 0, "test") == "test"
#     assert arrs.get([1, 2, 3], -1, "test") == "test"


@pytest.mark.parametrize('array, start, end, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, 3, [2, 3]),
    ([], 0, 0,  []),
    ([1, 2, 3], -4, 2, [1, 2]),
    ([1, 2, 3], -2, [2, 3])
])

def est_slice(array, start, end, expected):
    assert get(array, start, end) == expected


# Функция без фикстур
# def test_slice():
#     assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
#     assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
#     assert arrs.my_slice([], 0) == []
#     assert arrs.my_slice([1, 2, 3], -4, 2) == [1, 2]
#     assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
