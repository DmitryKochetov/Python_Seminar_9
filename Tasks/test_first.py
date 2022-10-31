# Написать тесты к функциям из ранее выполненных заданий.
import pytest
from first import find_quarter



@pytest.mark.parametrize('x, y, expected_result', [(34, -30, 4), (2, 4, 1), (-34, -30, 3), (-5, 5, 2)])
def test_find_quarter_good(x, y, expected_result):
    assert find_quarter(x, y) == expected_result

# test_find_quarter_good()

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
