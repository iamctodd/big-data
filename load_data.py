import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Set style for prettier plots
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# Load data and time it
start_time = time.time()
df = pd.read_csv('datasets/yelp_tiny_10k.csv')
load_time = time.time() - start_time

print(f"✓ Data loaded in {load_time:.2f} seconds")
print(f"Dataset shape: {df.shape}")
