# Medical Data Visualizer

This project completes the FreeCodeCamp Data Analysis with Python - Medical Data Visualizer project.

## Project Overview

This project visualizes and analyzes medical examination data using matplotlib, seaborn, and pandas. The dataset contains information about patients including body measurements, blood test results, and lifestyle choices, with a focus on exploring relationships with cardiovascular disease.

## Features Implemented

1. **Data Processing**
   - Loaded medical examination data from CSV
   - Added `overweight` column calculated from BMI (weight in kg / (height in m)²)
   - Normalized cholesterol and glucose values (0=normal, 1=above normal)

2. **Categorical Plot (`draw_cat_plot`)**
   - Created visualization showing counts of good/bad outcomes
   - Displays cholesterol, glucose, smoking, alcohol, physical activity, and overweight
   - Separate panels for patients with and without cardiovascular disease
   - Generated using seaborn's `catplot` with bar plot type

3. **Heatmap (`draw_heat_map`)**
   - Cleaned data by removing outliers:
     - Diastolic pressure > systolic pressure
     - Height < 2.5th percentile or > 97.5th percentile
     - Weight < 2.5th percentile or > 97.5th percentile
   - Calculated correlation matrix for all variables
   - Generated heatmap with lower triangle mask
   - Annotations show correlation coefficients with 1 decimal place

## Files

- `medical_data_visualizer.py` - Main implementation with draw_cat_plot() and draw_heat_map() functions
- `medical_examination.csv` - Dataset with 70,000 patient records
- `test_module.py` - Unit tests validating the implementation
- `main.py` - Entry point that runs the functions and executes tests
- `requirements.txt` - Python package dependencies
- `catplot.png` - Generated categorical plot visualization
- `heatmap.png` - Generated correlation heatmap visualization

## Installation

1. Install Python 3.10+
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

Execute the main script to generate visualizations and run tests:
```bash
python main.py
```

Or run tests directly:
```bash
python -m unittest test_module -v
```

## Test Results

All 4 unit tests pass:
- ✓ `test_line_plot_labels` - Validates categorical plot labels
- ✓ `test_bar_plot_number_of_bars` - Validates number of bars in chart
- ✓ `test_heat_map_labels` - Validates heatmap column labels  
- ✓ `test_heat_map_values` - Validates correlation coefficient annotations

## Data Description

**Columns:**
- `age` - Patient age in days
- `sex` - Gender (1=female, 2=male)
- `height` - Height in cm
- `weight` - Weight in kg
- `ap_hi` - Systolic blood pressure
- `ap_lo` - Diastolic blood pressure
- `cholesterol` - Cholesterol level (1=normal, 2=above normal, 3=well above normal)
- `gluc` - Glucose level (1=normal, 2=above normal, 3=well above normal)
- `smoke` - Smoking status (binary)
- `alco` - Alcohol intake (binary)
- `active` - Physical activity (binary)
- `cardio` - Presence of cardiovascular disease (binary target variable)
- `overweight` - Calculated BMI > 25 (binary)

## Project Status

✅ **COMPLETE** - All requirements met and tests passing.
