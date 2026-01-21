# Page View Time Series Visualizer

This project visualizes time series data from the freeCodeCamp forum using line charts, bar charts, and box plots.

## Project Overview

The project analyzes page view data from the freeCodeCamp forum from May 2016 to December 2019, creating three different visualizations to understand patterns in visits and identify yearly and monthly growth.

## Data

The dataset `fcc-forum-pageviews.csv` contains daily page view counts for the freeCodeCamp forum. The data has been cleaned by removing the top 2.5% and bottom 2.5% of values to eliminate outliers.

## Files

- `time_series_visualizer.py` - Main module containing all visualization functions
- `main.py` - Test script to generate all visualizations
- `test_module.py` - Unit tests for all functions
- `requirements.txt` - Project dependencies
- `fcc-forum-pageviews.csv` - Dataset file

## Functions

### `draw_line_plot()`
Creates a line chart showing daily page views over time. 
- Title: "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
- X-axis: Date
- Y-axis: Page Views
- Output: `line_plot.png`

### `draw_bar_plot()`
Creates a bar chart showing average daily page views for each month grouped by year.
- X-axis: Years
- Y-axis: Average Page Views
- Legend: Month labels with title "Months"
- Output: `bar_plot.png`

### `draw_box_plot()`
Creates two adjacent box plots showing distribution of page views:
1. Year-wise box plot showing trends over years
2. Month-wise box plot showing seasonal patterns
- Output: `box_plot.png`

## Requirements

- pandas
- matplotlib
- seaborn

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure the dataset file `fcc-forum-pageviews.csv` is in the same directory.

## Usage

Run the visualizations:
```bash
python main.py
```

Run the tests:
```bash
python -m unittest test_module -v
```

## Test Results

All 7 unit tests pass successfully:
- ✓ Line plot has correct title
- ✓ Line plot has correct labels
- ✓ Bar plot has correct labels
- ✓ Bar plot has legend with correct title
- ✓ Box plots are 2 in number
- ✓ Box plots have correct titles
- ✓ Box plots have correct axis labels

## Project Status

✅ Complete - All requirements met and all tests passing.
