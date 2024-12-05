from flask import Flask, request, jsonify, session
from flask_cors import CORS
import pickle
import pandas as pd
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
from database import User, SessionLocal

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Secret key for session management (should be secure in production)
app.secret_key = "supersecretkey"

# Load the trained model
with open('../model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Predict Route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        return jsonify({'prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Signup Route
@app.route('/signup', methods=['POST'])
def signup():
    try:
        # Connect to the database
        db: Session = SessionLocal()

        # Parse incoming data
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Check if the user already exists
        existing_user = db.query(User).filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            return jsonify({'error': 'User already exists!'}), 400

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Create a new user instance
        new_user = User(username=username, email=email, hashed_password=hashed_password)
        db.add(new_user)
        db.commit()

        return jsonify({'message': 'User created successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

# Login Route
@app.route('/login', methods=['POST'])
def login():
    try:
        # Connect to the database
        db: Session = SessionLocal()

        # Parse incoming data
        data = request.json
        username = data.get('username')
        password = data.get('password')

        # Check if the user exists
        user = db.query(User).filter(User.username == username).first()
        if not user:
            return jsonify({'error': 'Invalid username or password!'}), 400

        # Verify the password
        if not check_password_hash(user.hashed_password, password):
            return jsonify({'error': 'Invalid username or password!'}), 400

        # Create a session for the user
        session['user_id'] = user.id
        session['username'] = user.username

        return jsonify({'message': f'Welcome, {user.username}!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        db.close()

# Logout Route
@app.route('/logout', methods=['POST'])
def logout():
    try:
        session.clear()  # Clear all session data
        return jsonify({'message': 'Logged out successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Protected Route Example
@app.route('/protected', methods=['GET'])
def protected():
    if 'user_id' not in session:
        return jsonify({'error': 'You must be logged in to access this resource!'}), 401

    return jsonify({'message': f'Hello, {session["username"]}! This is a protected resource.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
