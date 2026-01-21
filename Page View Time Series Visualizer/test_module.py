import unittest
import time_series_visualizer
from unittest.mock import patch
import matplotlib.pyplot as plt


class LineChartTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_line_plot()

    def test_line_plot_labels(self):
        """Test line plot has correct labels"""
        ax = self.fig.axes[0]
        self.assertEqual(ax.get_xlabel(), 'Date')
        self.assertEqual(ax.get_ylabel(), 'Page Views')

    def test_line_plot_title(self):
        """Test line plot has correct title"""
        ax = self.fig.axes[0]
        self.assertEqual(ax.get_title(), 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    def tearDown(self):
        plt.close(self.fig)


class BarChartTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_bar_plot()

    def test_bar_plot_labels(self):
        """Test bar plot has correct labels"""
        ax = self.fig.axes[0]
        self.assertEqual(ax.get_xlabel(), 'Years')
        self.assertEqual(ax.get_ylabel(), 'Average Page Views')

    def test_bar_plot_legend(self):
        """Test bar plot has legend with correct title"""
        ax = self.fig.axes[0]
        legend = ax.get_legend()
        self.assertIsNotNone(legend)
        self.assertEqual(legend.get_title().get_text(), 'Months')

    def tearDown(self):
        plt.close(self.fig)


class BoxPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_box_plot()

    def test_box_plot_number_of_plots(self):
        """Test that there are 2 box plots"""
        self.assertEqual(len(self.fig.axes), 2)

    def test_box_plot_titles(self):
        """Test box plots have correct titles"""
        self.assertEqual(self.fig.axes[0].get_title(), 'Year-wise Box Plot (Trend)')
        self.assertEqual(self.fig.axes[1].get_title(), 'Month-wise Box Plot (Seasonality)')

    def test_box_plot_labels(self):
        """Test box plots have correct axis labels"""
        self.assertEqual(self.fig.axes[0].get_xlabel(), 'Year')
        self.assertEqual(self.fig.axes[0].get_ylabel(), 'Page Views')
        self.assertEqual(self.fig.axes[1].get_xlabel(), 'Month')
        self.assertEqual(self.fig.axes[1].get_ylabel(), 'Page Views')

    def tearDown(self):
        plt.close(self.fig)


if __name__ == '__main__':
    unittest.main()
