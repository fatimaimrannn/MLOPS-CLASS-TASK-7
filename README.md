MLOps Project with MLFlow, DVC, Airflow, and Full-Stack Application

Project Overview

This project demonstrates an end-to-end machine learning pipeline, incorporating MLOps best practices. It covers model versioning, data versioning, automated workflows, and deployment strategies using various tools such as MLFlow, DVC (Data Version Control), Airflow, Flask/FastAPI, React, and Kubernetes.

Project Objectives:
- Versioning machine learning models using MLFlow.
- Implementing data versioning using DVC.
- Automating workflows with Airflow.
- Creating a full-stack application with a weather prediction feature.
- Integrating CI/CD pipelines for development, testing, and production workflows.
- Deploying the application on Kubernetes (Minikube).

Project Structure

backend/
    ├── Dockerfile
    ├── app.py
    ├── requirements.txt
    └── tests/
frontend/
    ├── Dockerfile
    ├── src/
    └── package.json
dvc.yaml
mlflow_model/
    ├── model.py
    ├── requirements.txt
airflow/
    ├── dags/
    └── docker-compose.yml
.gitignore
README.md
docker-compose.yml

Tools & Technologies

- MLFlow: For model versioning, logging metrics and parameters, and model registry.
- DVC (Data Version Control): For versioning datasets and machine learning models.
- Airflow: For automating workflows, including data processing and model retraining.
- Flask/FastAPI: For backend API development to serve model predictions.
- React: For the frontend web application to interact with the API.
- Kubernetes/Minikube: For deploying the application in a containerized environment.
- GitHub Actions: For Continuous Integration (CI) and Continuous Deployment (CD) pipelines.
- SQLite/MySQL/MongoDB: For managing user authentication and session management.

Installation

Follow the steps below to set up the project locally.

1. Clone the Repository

git clone https://github.com/yourusername/your-repository-name.git
cd your-repository-name

2. Set Up DVC

Install DVC if you haven't already:

pip install dvc

To configure DVC and start versioning your data:

dvc init
dvc remote add -d myremote s3://mybucket/myfolder

3. Install Dependencies

Backend:

Navigate to the backend directory and install dependencies:

cd backend
pip install -r requirements.txt

Frontend:

Navigate to the frontend directory and install dependencies:

cd frontend
npm install

Airflow:

Install Airflow and required packages for automating workflows:

cd airflow
pip install -r requirements.txt

4. Set Up Database

For user authentication, choose a database like SQLite, MySQL, or MongoDB. Create and configure the database as needed, and set up the connection in the backend.

5. Run the Application

Backend API:

Start the backend server using Flask or FastAPI:

cd backend
python app.py

Frontend UI:

Start the frontend development server:

cd frontend
npm start

6. Running Airflow

To start Airflow, use Docker or the default setup:

cd airflow
docker-compose up

7. Run Unit Tests

To ensure everything works correctly, run the unit tests for the backend API:

cd backend/tests
pytest

8. Docker Setup

Build and run Docker containers for the application:

Backend:

cd backend
docker build -t your-backend-image .
docker run -p 5000:5000 your-backend-image

Frontend:

cd frontend
docker build -t your-frontend-image .
docker run -p 3000:3000 your-frontend-image

9. Deploying on Kubernetes (Minikube)

1. Set up Minikube on your local machine.
2. Create Kubernetes deployment manifests for the backend and frontend.
3. Deploy your application using kubectl:

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Workflow

MLFlow Versioning and Model Registry
- MLFlow is used to log models, hyperparameters, and metrics.
- Models are registered in the MLFlow Model Registry to manage stages (e.g., staging, production).
- Logs and metrics are tracked during the training phase.

DVC for Data Versioning
- DVC is used to track datasets and models during the project.
- Data and models are versioned and stored in a remote storage location.

Airflow Automation
- Airflow is used to automate the data pipeline and model retraining tasks.
- The DAG (Directed Acyclic Graph) in Airflow automates various stages such as data preprocessing, model training, and deployment.

CI/CD Pipeline
- GitHub Actions is configured to handle:
  - CI: Running unit tests and building Docker images.
  - CD: Deploying the application to the Kubernetes cluster.

Branch Workflow
- Dev Branch: For active development.
- Testing Branch: For running unit tests and CI pipeline.
- Prod Branch: For deploying the final application.

Running the Pipelines

CI Pipeline (Dev to Testing)
- Triggered when pushing changes to the testing branch.
- Runs unit tests and builds Docker images.
- Pushes the Docker images to DockerHub.

CD Pipeline (Testing to Prod)
- Triggered on merging to the prod branch.
- Deploys the application on Minikube using Kubernetes.

Blog Post

For more details, insights, and explanations of the project, please refer to my Medium blog (https://medium.com/@yourusername/project-blog).

Key Learnings

- Implemented MLFlow for model versioning and logging.
- Utilized DVC for data and model versioning in an MLOps pipeline.
- Automated workflows using Airflow for model training and monitoring.
- Integrated CI/CD pipelines for smooth deployment using GitHub Actions and Minikube.

License

This project is licensed under the MIT License - see the LICENSE file for details.
