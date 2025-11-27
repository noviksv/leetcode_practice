"""Tests for Two Sum problem."""

import unittest
from problems.two_sum import Solution


class TestTwoSum(unittest.TestCase):
    """Test cases for the Two Sum solution."""

    def setUp(self):
        """Set up test fixtures."""
        self.solution = Solution()

    def test_example_1(self):
        """Test with nums = [2,7,11,15], target = 9."""
        result = self.solution.two_sum([2, 7, 11, 15], 9)
        self.assertEqual(sorted(result), [0, 1])

    def test_example_2(self):
        """Test with nums = [3,2,4], target = 6."""
        result = self.solution.two_sum([3, 2, 4], 6)
        self.assertEqual(sorted(result), [1, 2])

    def test_example_3(self):
        """Test with nums = [3,3], target = 6."""
        result = self.solution.two_sum([3, 3], 6)
        self.assertEqual(sorted(result), [0, 1])

    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = self.solution.two_sum([-1, -2, -3, -4, -5], -8)
        self.assertEqual(sorted(result), [2, 4])

    def test_zero_target(self):
        """Test with zero as target."""
        result = self.solution.two_sum([-3, 4, 3, 90], 0)
        self.assertEqual(sorted(result), [0, 2])


if __name__ == "__main__":
    unittest.main()
