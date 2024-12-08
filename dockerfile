# Use Python as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the db directory exists
RUN mkdir -p /app/db

# Copy the model file into the Docker container
COPY model.pkl .

# Copy the application source code
COPY . .

# Expose the app port (adjust this based on your Flask app port)
EXPOSE 5000

# Define the command to run your Flask app
CMD ["python", "backend/app.py"]  # Adjust this to your Flask entry point file
