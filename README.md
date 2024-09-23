# Python Technical test
This repository contains a Python-based technical test for a position at AHT Global. The project involves a Dockerized setup to run a Python application using specific dependencies and configurations.

Table of Contents
1. Project Overview
2. Requirements
3. Installation
4. Usage
5. File Structure
6. Running with Docker

## Project Overview
This project is designed to demonstrate technical proficiency in Python development, Docker, and working with a pre-configured application environment. The app consists of several services running via Docker, ensuring easy deployment and scalability.

## Requirements
Python 3.x
Docker & Docker Compose
Installation
1. Clone the Repository:
To get started, clone the repository to your local machine:

bash
`git clone https://github.com/Danielpviana/PythonDevTechnicalTest.git
cd PythonDevTechnicalTest`
2. Install Python Dependencies:
If you plan to run the app outside Docker, first install the required Python dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Running Locally
Once the dependencies are installed, you can start using the application. Make sure to set up any necessary environment variables or configuration files as per your requirements.

bash
Copy code
python app/main.py
Running Tests
To run tests for the application:

bash
Copy code
pytest


## File Structure
plaintext
Copy code
PythonDevTechnicalTest/
│
├── app/                  # Main application code
│   ├── __init__.py
│   ├── main.py           # Entry point of the app
│   └── tests/            # Unit tests
│
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Docker Compose for multi-container setup
├── requirements.txt      # Python dependencies
└── .gitignore            # Git ignore file
Running with Docker
1. Build Docker Image:
You can build the Docker image for the project using the following command:

bash
Copy code
docker-compose build
2. Start the Application:
Use Docker Compose to start the services. It will automatically set up the necessary containers and network.

bash
Copy code
docker-compose up
The application will be available at http://localhost:8000 (or any specified port).

3. Shut Down the Application:
To stop and remove the containers:

bash
Copy code
docker-compose down
Contributing
Contributions are welcome! Please open a pull request with any improvements or bug fixes. Ensure your code passes all tests before submitting.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
