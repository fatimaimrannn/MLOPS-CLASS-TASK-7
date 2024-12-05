import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://localhost:5000")
# Step 1: Load the preprocessed data
processed_data_file = "processed_data.csv"
df = pd.read_csv(processed_data_file)

# Step 2: Verify column names to ensure they are as expected
print("Columns in the dataset:", df.columns)

# Step 3: Define features (X) and target (y)
X = df[['Humidity', 'Wind Speed']]  # Features
y = df['Temperature']  # Target

# Step 4: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Initialize and train the linear regression model
model = LinearRegression()

# Step 6: Start an MLFlow run to log parameters, metrics, and the model
with mlflow.start_run():

    # Log hyperparameters (in this case, model configuration)
    mlflow.log_param("model_type", "LinearRegression")
    
    # Train the model
    model.fit(X_train, y_train)

    # Step 7: Print the model's score (R-squared) on the test set
    r_squared = model.score(X_test, y_test)
    print("Model R-squared on test data:", r_squared)

    # Log the metric (R-squared value)
    mlflow.log_metric("r_squared", r_squared)
    
    # Step 8: Save the trained model to a pickle file
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    
    # Log the model in MLFlow
    mlflow.sklearn.log_model(model, "model")

    print("Model saved as model.pkl")
