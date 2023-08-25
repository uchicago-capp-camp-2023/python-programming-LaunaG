"""is_square.py
"""
from practice import is_square


class TestSquare:
    """Unit tests for validating the square definition exercise."""

    def test_unit_square_is_square(self):
        """is_square([0, 0], [0, 1], [1, 1], [1, 0])"""
        val = is_square([0, 0], [0, 1], [1, 1], [1, 0])
        assert val == True

    def test_negative_unit_square_is_square(self):
        """is_square([0, 0], [0, -1], [-1, -1], [-1, 0])"""
        val = is_square([0, 0], [0, -1], [-1, -1], [-1, 0])
        assert val == True

    def test_unequal_sides_is_not_square(self):
        """is_square([0, 0], [0, 1], [1, 1], [1, 2])"""
        val = is_square([0, 0], [0, 1], [1, 1], [1, 2])
        assert val == False

    def test_line_is_not_square(self):
        """is_square([-1, 0], [0, 0], [1, 0], [2, 0])"""
        val = is_square([-1, 0], [0, 0], [1, 0], [2, 0])
        assert val == False

    def test_overlapping_pts_is_not_square(self):
        """is_square([1, 1], [1, 1], [2, 2], [2, 2])"""
        val = is_square([1, 1], [1, 1], [2, 2], [2, 2])
        assert val == False
