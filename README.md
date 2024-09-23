# Python Technical test
This repository contains a Python-based technical test for a position at AHT Global. The project involves a Dockerized setup to run a Python application using specific dependencies and configurations.

## Table of Contents
1. Project Overview
2. Requirements
3. Installation
4. Docker deployment
5. File Structure
6. Shutdown application

## Project Overview
This project is designed to demonstrate technical proficiency in Python development, Docker, and working with a pre-configured application environment. The app consists of several services running via Docker, ensuring easy deployment and scalability.

## Requirements
Python 3.x

Docker & Docker Compose

## Installation
1. **Clone the Repository**:
To get started, clone the repository to your local machine:

```PowerShell
git clone https://github.com/Danielpviana/PythonDevTechnicalTest.git
```

2. **Install Python Dependencies**:
If you plan to run the app outside Docker, first install the required Python dependencies:

```PowerShell
pip install -r requirements.txt
```

3. **Running Locally**:
Once the dependencies are installed, you can start using the application. Make sure to set up any necessary environment variables or configuration files as per your requirements.

```PowerShell
python -m flask --app ./app/main.py run
```

Once the web application is running, it can be accessed through port `[localhost:5000]`

## Docker deployment 
**Running docker containers**

Deploy the application by running docker-compose.

```PowerShell
docker-compose -f docker-compose.yml up --build
```

Once the web application is running in a separate container, it can be accessed through port `[localhost:5000](http://127.0.0.1:5000)`

Database communication occurs through docker localhost port `[localhost:3306]`

## File Structure
PythonDevTechnicalTest/
```
│
├── app/                  # Main application code
│   ├── app_config.py     # Application setup
│   ├── db_config.py      # Database setup
│   ├── main.py           # Entry point of the app
│   ├── models.py         # Object definition for database table creation
│   ├── routes.py         # Routing services for database transactions
│   └── templates/        # Jinja2 templates for views
│       ├── add.html      # Addition or modification of products
│       ├── base.html     # Main layout for general views
│       ├── index.html    # Main view
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Docker Compose for multi-container setup
├── requirements.txt      # Python dependencies
└── .gitignore            # Git ignore file
```

## Shutdown the Application:
To stop and remove the containers:

```Powershell
docker-compose down
```
