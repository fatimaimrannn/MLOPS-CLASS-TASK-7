import requests

# Define the URL and data
url = "http://127.0.0.1:5000/predict"
data = {
    "Humidity": 50,  # Match feature names from model training
    "Wind Speed": 5
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response
print("Response:", response.json())
