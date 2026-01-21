# Sea Level Predictor

This project analyzes the global average sea level change since 1880 and predicts future sea level rise through 2050 using linear regression.

##  Features

- Loads sea level data from CSV file
- Creates a scatter plot of historical sea level measurements
- Fits two linear regression models:
  1. Using all available data (1880-2014) to predict trends through 2050
  2. Using recent data (2000-2014) to predict trends if current rate continues through 2050
- Generates visualization with both regression lines extending to year 2050
- Saves the resulting plot as 'sea_level_plot.png'

## Files

- `sea_level_predictor.py` - Main module containing the `draw_plot()` function
- `epa-sea-level.csv` - Historical sea level data from EPA
- `test_module.py` - Unit tests
- `main.py` - Development/testing entry point

## Requirements

- pandas >= 2.0.3
- matplotlib >= 3.8.1
- scipy >= 1.11.4

## Usage

```python
import sea_level_predictor

# Generate the plot and return the axes object
ax = sea_level_predictor.draw_plot()
```

The plot will be saved as `sea_level_plot.png` showing:
- Blue scatter points: Actual sea level measurements  
- Red line: Projection based on all historical data (1880-2050)
- Green line: Projection based on recent data (2000-2050)

## Testing

Run the unit tests with:
```bash
python main.py
```

Or directly with pytest/unittest:
```bash
python -m unittest test_module
```
