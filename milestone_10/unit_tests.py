import unittest
from unittest.mock import patch
from data.app import filter_employees

class MockCSVReader:
    def __init__(self, data):
        self.data = data
        self.line_num = 0  # Initialize line_num

    def __iter__(self):
        # Create an iterator that increments line_num each time a row is yielded
        for row in self.data:
            self.line_num += 1
            yield row

class TestDataFiltering(unittest.TestCase):
    @patch('csv.DictReader')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="name,hire_date,department,birthday\nJohn Doe,2020-01-15,Engineering,1990-04-25\n")
    def test_filter_employees_by_month_and_department(self, mock_open, mock_csv_reader):
        # Setup the mock to use our custom MockCSVReader
        mock_data = [
            {"name": "John Doe", "hire_date": "2020-01-15", "department": "Engineering", "birthday": "1990-04-25"}
        ]
        mock_csv_reader.side_effect = lambda *args, **kwargs: MockCSVReader(mock_data)

        # Call the function under test
        result = filter_employees('fake_file.csv', 4, 'Engineering', 'birthday')

        # Expected result, considering the mock data and filter criteria
        expected = [
            {"id": 1, "name": "John Doe", "birthday": "Apr 25"}  # Use the same date format as the function's output
        ]

        self.assertEqual(result, expected)
        mock_open.assert_called_once_with('fake_file.csv', 'r')

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)