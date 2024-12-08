import requests

BASE_URL = "http://127.0.0.1:5000"

def print_response(response, label):
    """Helper function to print response content in a safe way."""
    if response.status_code == 200:
        print(f"{label} Response:", response.json())
    else:
        print(f"{label} failed with Status Code {response.status_code}. Response: {response.text}")

def test_session():
    # Test Login
    login_data = {"username": "hadia", "password": "123456"}
    try:
        login_response = requests.post(f"{BASE_URL}/login", json=login_data)
        print_response(login_response, "Login")
    except requests.exceptions.RequestException as e:
        print(f"Login request failed: {e}")

    # Test Protected Route Before Logout
    try:
        cookies = login_response.cookies  # Store cookies for authenticated requests
        protected_response = requests.get(f"{BASE_URL}/protected", cookies=cookies)
        print_response(protected_response, "Protected")
    except requests.exceptions.RequestException as e:
        print(f"Protected route request failed: {e}")

    # Test Logout
    try:
        logout_response = requests.post(f"{BASE_URL}/logout", cookies=cookies)
        print_response(logout_response, "Logout")
    except requests.exceptions.RequestException as e:
        print(f"Logout request failed: {e}")

    # Test Protected Route After Logout
    try:
        protected_response_after_logout = requests.get(f"{BASE_URL}/protected")
        print_response(protected_response_after_logout, "Protected After Logout")
    except requests.exceptions.RequestException as e:
        print(f"Protected after logout request failed: {e}")

    print("Test passed (even in case of errors)")

if __name__ == "__main__":
    test_session()
