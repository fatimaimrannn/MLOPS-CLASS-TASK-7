import requests

BASE_URL = "http://127.0.0.1:5000"

def test_session():
    # Test Login
    login_data = {"username": "testuser", "password": "securepassword"}
    login_response = requests.post(f"{BASE_URL}/login", json=login_data)
    print("Login Response:", login_response.json())

    # Test Protected Route Before Logout
    cookies = login_response.cookies  # Store cookies for authenticated requests
    protected_response = requests.get(f"{BASE_URL}/protected", cookies=cookies)
    print("Protected Response:", protected_response.json())

    # Test Logout
    logout_response = requests.post(f"{BASE_URL}/logout", cookies=cookies)
    print("Logout Response:", logout_response.json())

    # Test Protected Route After Logout
    protected_response_after_logout = requests.get(f"{BASE_URL}/protected")
    print("Protected After Logout:", protected_response_after_logout.json())

if __name__ == "__main__":
    test_session()
