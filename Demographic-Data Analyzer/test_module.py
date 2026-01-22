import unittest
import demographic_data_analyzer as analyzer
import pandas as pd

class TestDemographicAnalyzer(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv('adult.data.csv')
    
    def test_data_loaded(self):
        """Test that data is loaded correctly"""
        self.assertGreater(len(self.df), 0)
        self.assertIn('race', self.df.columns)
        self.assertIn('salary', self.df.columns)

if __name__ == '__main__':
    unittest.main()
