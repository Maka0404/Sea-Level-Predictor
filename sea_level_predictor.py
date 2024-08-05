import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')
    
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')
    
    regress_results = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series(range(df['Year'].min(), 2051))
    y = regress_results.intercept + regress_results.slope * x
    plt.plot(x, y, 'r', label='Fit Line (1880 onwards)')
    
    df_recent = df[df['Year'] >= 2000]
    regress_results_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = regress_results_recent.intercept + regress_results_recent.slope * x_recent
    plt.plot(x_recent, y_recent, 'g', label='Fit Line (2000 onwards)')
    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    plt.savefig('sea_level_plot.png')
    return plt.gca()
