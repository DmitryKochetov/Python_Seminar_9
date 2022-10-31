# Написать тесты к функциям из ранее выполненных заданий.

import pytest
from second import find_distance


@pytest.mark.parametrize('ax, ay, bx, by, expected_result', [(3, 6, 2, 1, 5.09), (7, -5, 1, -1, 7.21)])
def test_find_distance_good(ax, ay, bx, by, expected_result):
    assert find_distance(ax, ay, bx, by) == expected_result

    # - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# def find_distance(ax,ay,bx,by):
#     return ((ax-bx)**2+(ay-by)**2)**(0.5)