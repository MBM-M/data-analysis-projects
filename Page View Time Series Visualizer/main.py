import matplotlib.pyplot as plt
import time_series_visualizer

# Test the functions
print("Generating Line Plot...")
fig1 = time_series_visualizer.draw_line_plot()
print("Line plot saved as line_plot.png")

print("\nGenerating Bar Plot...")
fig2 = time_series_visualizer.draw_bar_plot()
print("Bar plot saved as bar_plot.png")

print("\nGenerating Box Plots...")
fig3 = time_series_visualizer.draw_box_plot()
print("Box plots saved as box_plot.png")

print("\nAll visualizations have been generated!")
plt.show()
