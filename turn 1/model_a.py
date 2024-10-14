import unittest
from typing import List, Tuple

def aggregate_data(data: List[int]) -> int:
	"""
	A simple aggregation function that sums up a list of integers
	"""
	return sum(data)

class TestAggregationFunction(unittest.TestCase):

	def test_aggregate_data_with_empty_list(self):
		expected_output = 0
		result = aggregate_data([])
		self.assertEqual(result, expected_output, "Aggregation failed for empty list")

	def test_aggregate_data_with_single_element_list(self):
		expected_output = 42
		result = aggregate_data([42])
		self.assertEqual(result, expected_output, "Aggregation failed for a single element list")

	def test_aggregate_data_with_multiple_elements(self):
		test_cases: List[Tuple[List[int], int]] = [
			([1, 2, 3], 6),
			([10, 20, 30], 60),
			([-1, -2, -3], -6),
		]
		for input_data, expected_output in test_cases:
			with self.subTest(input_data=input_data):
				result = aggregate_data(input_data)
				self.assertEqual(result, expected_output, f"Aggregation failed for input: {input_data}")

if __name__ == '__main__':
	unittest.main()
