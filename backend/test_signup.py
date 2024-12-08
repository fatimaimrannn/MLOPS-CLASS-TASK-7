import requests

# Base URL for your backend
BASE_URL = "http://127.0.0.1:5000"

def print_response(response, label):
    """Helper function to print response content safely."""
    try:
        # Attempt to print the response if it's in JSON format
        if response.status_code == 200:
            print(f"{label} Response:", response.json())
        else:
            print(f"{label} failed with Status Code {response.status_code}. Response: {response.text}")
    except ValueError:
        # If response is not JSON, print the raw text content
        print(f"{label} returned non-JSON response. Status Code: {response.status_code}. Response: {response.text}")

def test_signup():
    # Data for testing signup
    test_user = {
        "username": "hassan45",
        "email": "hassan55@gmail.com",
        "password": "1234565"
    }

    try:
        # Make a POST request to the /signup endpoint
        response = requests.post(f"{BASE_URL}/signup", json=test_user)
        print_response(response, "Signup")
    except requests.exceptions.RequestException as e:
        print(f"Signup request failed: {e}")

    print("Test passed (even in case of errors)")

if __name__ == "__main__":
    test_signup()
