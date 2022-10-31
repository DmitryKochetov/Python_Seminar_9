# Написать тесты к функциям из ранее выполненных заданий.

import pytest
from third import conv_to_bin


@pytest.mark.parametrize('n, expected_result', [(45, '101101'), (3, '11'), (2, '10')])
def test_conv_to_bin(n, expected_result):
    assert conv_to_bin(n) == expected_result



