"""test_fizzbuzz.py
"""
from practice import fizzbuzz


class TestFizzBuzz:
    """Unit tests for validating the FizzBuzz exercise."""

    def test_100_is_buzz(self):
        """fizzbuzz(100)"""
        val = fizzbuzz(100)
        assert val == "Buzz!"

    def test_13_is_number(self):
        """fizzbuzz(13)"""
        val = fizzbuzz(13)
        assert val == "13"

    def test_3_is_fizz(self):
        """fizzbuzz(3)"""
        val = fizzbuzz(3)
        assert val == "Fizz!"

    def test_60_is_fizzbuzz(self):
        """fizzbuzz(60)"""
        val = fizzbuzz(60)
        assert val == "FizzBuzz!"
