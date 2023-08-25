"""test_max_integer.py
"""
from practice import max_integer


class TestMaxInteger:
    """Unit tests for validating the max integer exercise."""

    def test_max(self):
        """max_integer(89, 201, 99)"""
        val = max_integer(89, 201, 99)
        assert val == 201

    def test_max_with_negatives(self):
        """max_integer(-1, -568, 0)"""
        val = max_integer(-1, -568, 0)
        assert val == 0

    def test_max_with_repeats(self):
        """max_integer(-50, -50, -100)"""
        val = max_integer(-50, -50, -100)
        assert val == -50
