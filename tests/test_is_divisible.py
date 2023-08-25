"""test_divisibility.py
"""
from practice import is_divisible


class TestDivisibility:
    """Unit tests for validating the divisiblity exercise."""

    def test_10_is_divisible_by_5(self):
        """is_divisible(10, 5)"""
        val = is_divisible(10, 5)
        assert val == True

    def test_1_is_not_divisible_by_33(self):
        """is_divisible(1, 33)"""
        val = is_divisible(1, 33)
        assert val == False

    def test_33_is_divisible_by_1(self):
        """is_divisible(33, 1)"""
        val = is_divisible(33, 1)
        assert val == True
