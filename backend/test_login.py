import requests

# Base URL for your backend
BASE_URL = "http://127.0.0.1:5000"

def test_login():
    # Data for testing login
    login_data = {
        "username": "testuserr",
        "password": "securepassword"
    }

    # Make a POST request to the /login endpoint
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    
    # Print the response
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

if __name__ == "__main__":
    test_login()
