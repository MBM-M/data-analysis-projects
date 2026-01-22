import unittest
import mean_var_std
from io import StringIO
import sys

class TestMeanVarianceStdDev(unittest.TestCase):
    
    def test_correct_list_length(self):
        """Test with correct list length (9 numbers)"""
        # This should not raise an error
        captured_output = StringIO()
        sys.stdout = captured_output
        mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn('mean', output)
    
    def test_incorrect_list_length(self):
        """Test with incorrect list length"""
        captured_output = StringIO()
        sys.stdout = captured_output
        mean_var_std.calculate([1, 2, 3])
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertIn('List must contain nine numbers', output)

if __name__ == '__main__':
    unittest.main()
