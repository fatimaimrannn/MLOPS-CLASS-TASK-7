import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Step 1: Load the preprocessed data
processed_data_file = "processed_data.csv"
df = pd.read_csv(processed_data_file)

# Step 2: Verify column names to ensure they are as expected
print("Columns in the dataset:", df.columns)

# Step 3: Define features (X) and target (y)
# We are using 'Wind Speed' and 'Humidity' as features to predict 'Temperature'
X = df[['Humidity', 'Wind Speed']]  # Features
y = df['Temperature']  # Target

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Print the model's score (R-squared) on the test set
print("Model R-squared on test data:", model.score(X_test, y_test))

# Step 7: Save the trained model to a pickle file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as model.pkl")
