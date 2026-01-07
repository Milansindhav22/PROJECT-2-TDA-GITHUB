"""
Helper Functions for Data Analysis Portfolio
Reusable functions across all projects
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(filename, data_folder='../../data'):
    """
    Load CSV file from data folder with error handling
    
    Args:
        filename (str): Name of the CSV file
        data_folder (str): Path to data folder (default: ../../data)
    
    Returns:
        DataFrame or None: Loaded data or None if file not found
    """
    filepath = os.path.join(data_folder, filename)
    
    try:
        df = pd.read_csv(filepath)
        print(f"✅ Successfully loaded {filename}")
        print(f"   Shape: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print(f"❌ Error: Could not find {filename} in {data_folder}")
        return None
    except Exception as e:
        print(f"❌ Error loading {filename}: {str(e)}")
        return None

def save_plot(filename, folder='outputs', dpi=300):
    """
    Save the current matplotlib plot to file
    
    Args:
        filename (str): Name for the saved file (e.g., 'sales_trend.png')
        folder (str): Folder to save in (default: 'outputs')
        dpi (int): Resolution (default: 300)
    """
    # Create folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)
    
    # Save the plot
    filepath = os.path.join(folder, filename)
    plt.savefig(filepath, dpi=dpi, bbox_inches='tight')
    print(f"✅ Saved plot: {filepath}")
    plt.close()

def setup_plot_style():
    """
    Apply consistent styling to all plots
    """
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['legend.fontsize'] = 10

def print_summary(df, title="Dataset Summary"):
    """
    Print a formatted summary of the dataset
    
    Args:
        df (DataFrame): The dataset to summarize
        title (str): Title for the summary
    """
    print("\n" + "="*50)
    print(f"{title}")
    print("="*50)
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"\nColumns: {', '.join(df.columns.tolist())}")
    print(f"\nMissing values:\n{df.isnull().sum()}")
    print(f"\nData types:\n{df.dtypes}")
    print("="*50 + "\n")