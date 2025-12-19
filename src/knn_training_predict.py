from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
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

# 1. Split into Features (X) and Target (y)
X = df[['Weight', 'Texture']]
y = df['Label']

# 2. Split into Training and Testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Initialize the model (let's use k=3)
knn = KNeighborsClassifier(n_neighbors=3)

# 4. Train the model
knn.fit(X_train, y_train)

# 5. Predict a new fruit: 170g with a texture of 4
new_fruit = [[170, 4]]
prediction = knn.predict(new_fruit)
print(f"Prediction for {new_fruit}: {'Orange' if prediction[0] == 1 else 'Apple'}")