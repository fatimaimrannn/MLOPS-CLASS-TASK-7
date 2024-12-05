import requests

# Base URL for your backend
BASE_URL = "http://127.0.0.1:5000"

def test_signup():
    # Data for testing signup
    test_user = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "securepassword"
    }

    # Make a POST request to the /signup endpoint
    response = requests.post(f"{BASE_URL}/signup", json=test_user)
    
    # Print the response
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

if __name__ == "__main__":
    test_signup()
