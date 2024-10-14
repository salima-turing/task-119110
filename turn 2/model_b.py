import unittest
from parameterized import parameterized

def average(numbers):
    total = sum(numbers)
    return total / len(numbers)

class TestAverageFunction(unittest.TestCase):

    @parameterized.expand([
        ([1, 2, 3], 2),
        ([10, 20, 30], 20),
        ([-1, 0, 1], 0),
        ([], 0),
        ([42], 42),
    ])
    def test_average_with_parameterized_data(self, input_data, expected_average):
        result = average(input_data)
        self.assertEqual(result, expected_average, f"Average calculation failed for input: {input_data}")

if __name__ == '__main__':
    unittest.main()
