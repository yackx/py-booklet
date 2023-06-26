import pytest

from booklet import order_booklet


@pytest.mark.parametrize("number_of_pages, expected_order", [
    (4, [4, 1, 2, 3]),
    (8, [8, 1, 2, 7, 6, 3, 4, 5]),
    (36, [36, 1, 2, 35, 34, 3, 4, 33, 32, 5, 6, 31, 30, 7, 8, 29, 28, 9, 10, 27, 26, 11, 12, 25, 24, 13, 14, 23, 22, 15, 16, 21, 20, 17, 18, 19])
])
def test_order_booklet(number_of_pages, expected_order):
    assert order_booklet(number_of_pages) == expected_order
