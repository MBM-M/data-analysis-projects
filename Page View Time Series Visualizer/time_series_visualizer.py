import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# Clean data - remove top 2.5% and bottom 2.5%
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Create figure and plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(df.index, df['value'], color='blue', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.grid(True, alpha=0.3)
    
    fig.tight_layout()
    plt.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy data and create year and month columns
    df_copy = df.copy()
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month
    
    # Calculate average page views per month per year
    df_bar = df_copy.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Create figure and plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot bar chart
    df_bar.plot(kind='bar', ax=ax, width=0.8)
    
    ax.set_title('Average Daily Page Views - Each Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    
    # Month labels
    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax.legend(month_labels, title='Months', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    fig.tight_layout()
    plt.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Copy data and create year and month columns
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month
    df_box['month_name'] = df_box.index.strftime('%b')
    
    # Create subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Year-wise box plot
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise box plot
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month_name', y='value', order=month_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    fig.tight_layout()
    plt.savefig('box_plot.png')
    return fig
