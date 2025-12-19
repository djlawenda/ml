import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate 20 Apples (Label 0) - Usually lighter and smoother
apples = pd.DataFrame({
    'Weight': np.random.normal(140, 15, 20),
    'Texture': np.random.normal(8, 1, 20),
    'Name' : 'apple',
    'Label': 0
})

# Generate 20 Oranges (Label 1) - Usually heavier and rougher
oranges = pd.DataFrame({
    'Weight': np.random.normal(180, 20, 20),
    'Texture': np.random.normal(3, 1, 20),
    'Name' : 'orange',
    'Label': 1
})

# Combine into one DataFrame
df = pd.concat([apples, oranges]).sample(frac=1).reset_index(drop=True)

print(df.head())

