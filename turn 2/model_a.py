import unittest
from parameterized import parameterized
from typing import List

# Rest of the code remains the same
def aggregate_data(data: List[int]) -> int:
	"""
	A simple aggregation function that sums up a list of integers
	"""
	return sum(data)

class TestAggregationFunction(unittest.TestCase):

	@parameterized.expand([
		([], 0),
		([42], 42),
		([1, 2, 3], 6),
		([10, 20, 30], 60),
		([-1, -2, -3], -6),
	])
	def test_aggregate_data(self, input_data, expected_output):
		result = aggregate_data(input_data)
		self.assertEqual(result, expected_output, f"Aggregation failed for input: {input_data}")

if __name__ == '__main__':
	unittest.main()
