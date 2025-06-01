# Car Dealership Review Portal (IBM Full Stack Capstone Project)

This repository contains the source code for the "Car Dealership Review Portal", developed as part of the **IBM Full Stack Software Developer Professional Certificate**. The project aims to centralize and manage customer reviews for a national car dealership's various branches, promoting transparency and customer trust.

## Table of Contents

* [Project Description](#project-description)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Project Architecture](#project-architecture)
* [Setup and Local Development](#setup-and-local-development)
* [Deployment](#deployment)
* [Prerequisites](#prerequisites)
* [Contact](#contact)
* [License](#license)

## Project Description

Responding to a national car dealership's need to centralize branch reviews, this project involves creating a comprehensive web platform that allows customers to:

1.  Search for and view branch information by state.
2.  Browse existing customer reviews for different branches.
3.  Register, log in, and submit their own reviews for any branch.

The system is designed to enhance customer interaction with the dealership, offering a single point for feedback and increasing trust through transparency.

## Features

* **Branch Search:** Filter and display dealership branches by state.
* **Review Viewing:** Access all customer reviews for each branch, including dynamic display of details.
* **User Authentication:** User registration, login, and logout functionalities with session management.
* **Review Submission:** Registered users can post new reviews for any branch, with details like purchase date, car make, and year.
* **Sentiment Analysis Integration:** Implemented a sentiment analyzer microservice (Python, Flask, NLTK) deployed on IBM Cloud Code Engine to process and categorize review sentiment.
* **Dynamic Pages:** Creation of dynamic React pages for viewing dealership details and adding reviews.
* **Static Pages:** Developed static web pages using HTML, CSS, and Bootstrap.
* **Containerization:** Application components are containerized using Docker for efficient management and deployment.
* **Kubernetes Orchestration:** Includes deployment artifacts for managing the application with Kubernetes.

## Technologies Used

This Full Stack project was built using a combination of modern technologies for the frontend, backend, and deployment:

* **Frontend:**
    * HTML5
    * CSS3
    * JavaScript
    * React
    * Bootstrap
* **Backend:**
    * Python
    * Django / Flask (web frameworks for core backend logic)
    * Node.js
    * Express.js (for backend services connecting with MongoDB)
    * SQL (PostgreSQL, MySQL)
    * MongoDB (database for Node.js/Express services)
* **Tools & Deployment:**
    * Git / GitHub (version control, CI/CD with GitHub Actions for linting)
    * Docker (containerization of services, including MongoDB and Express server)
    * Kubernetes (orchestration of containers and application management)
    * IBM Cloud Code Engine (for deploying microservices, e.g., sentiment analysis)
    * Natural Language Toolkit (NLTK) and Flask (for sentiment analysis microservice)
    * `gunicorn` (WSGI HTTP server for Python web applications)

## Project Architecture

The application adopts a hybrid cloud strategy and a microservices architecture with a Full Stack structure:

* **Frontend (React.js):** Serves the interactive user interface, rendering static and dynamic pages. It communicates with backend services via APIs.
* **Backend (Django/Flask):** Handles core business logic, user management (registration, login, session management), and interacts with the SQL database.
* **Backend Services (Node.js/Express with MongoDB):** Containerized with Docker, these provide API endpoints for accessing specific dealership and review data.
* **Sentiment Analysis Microservice (Python/Flask/NLTK):** Deployed on IBM Cloud Code Engine, this service processes and analyzes the sentiment of reviews.
* **Containerization and Orchestration:** Docker is used for building and pushing images to IBM Cloud Image Registry (ICR), and Kubernetes artifacts are included for deployment and management.

## Setup and Local Development

To set up and run the project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Kxtss/xrwvm-fullstack_developer_capstone.git
    ```
2.  **Configure the Django Backend:**
    * Navigate to the `server` directory.
    * Install Python dependencies:
        ```bash
        pip install virtualenv
        virtualenv djangoenv
        source djangoenv/bin/activate
        pip install -Ur requirements.txt
        ```
    * Perform database migrations:
        ```bash
        python manage.py makemigrations --noinput
        python manage.py migrate --noinput
        python manage.py collectstatic --noinput
        ```
    * Define necessary environment variables (e.g., database connections, secret keys).
    * The Django application is configured to run with `gunicorn` on port 8000.
3.  **Configure Node.js/Express Backend Services:**
    * Navigate to the `server/database` directory (or where your Express services are located).
    * Install Node.js dependencies:
        ```bash
        npm install
        ```
    * Ensure MongoDB is running (you can use Docker for this as per Docker Compose instructions below).
    * Start the Express server.
4.  **Configure the React Frontend:**
    * Navigate to the `server/frontend` directory.
    * Install Node.js dependencies:
        ```bash
        npm install
        ```
    * Build the frontend:
        ```bash
        npm run build
        ```
5.  **Build and Push Docker Images:**
    * From the `server` directory, build the Docker image:
        ```bash
        docker build -t us.icr.io/$MY_NAMESPACE/dealership .
        ```
        (Replace `$MY_NAMESPACE` with your actual IBM Cloud namespace, which can be exported via `ibmcloud cr namespaces | grep sn-labs-`.)
    * Push the image to IBM Cloud Image Registry (ICR):
        ```bash
        docker push us.icr.io/$MY_NAMESPACE/dealership
        ```
6.  **Run with Docker Compose (Recommended for Local Dev):**
    * The project can be orchestrated locally using Docker Compose, bringing up all containerized services (MongoDB, Express server, and the main application).
    * Use `docker-compose up --build` from the root directory of the project.
7.  **Access the Application:**
    * Open your web browser and navigate to the URL where the application is running (typically `http://localhost:8000` or the port configured in your Docker Compose).

## Deployment

The project is designed for robust deployment with CI/CD practices:

* **Containerization:** All main components, including the Django application, Node.js/Express backend, and MongoDB, are containerized using Docker.
* **Kubernetes Orchestration:** Deployment artifacts (`deployment.yaml`) are provided to manage the application on a Kubernetes cluster.
* **Continuous Integration/Continuous Delivery (CI/CD):** Configured with GitHub Actions for automated linting and potentially other CI/CD pipelines.
* **Cloud Microservices:** The sentiment analysis microservice is independently deployed and accessible via IBM Cloud Code Engine.

## Prerequisites

Ensure you have the following installed before running the project:

* Node.js (LTS version recommended)
* Python (3.x version recommended)
* pip (Python package installer)
* Docker and Docker Compose
* Git

## Contact

If you have any questions or suggestions, feel free to contact me:

* **discord:** tengokudaimakyo
* **Email:** x.kxtss@outlook.es

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
