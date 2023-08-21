# Flask_ORM_RestFul - Setup Guide

Welcome to the setup guide for the **Project Name** application. This guide will walk you through the process of setting up a virtual environment and running the application on your local machine.

## Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python 3.6 or higher
- pip (Python package manager)

## Setup Instructions

1. **Clone the Repository:**

   Open your terminal and navigate to the directory where you want to store the project. Run the following command to clone the repository:

   git clone https://github.com/ArunLR12/Flask_ORM_RestFul.git

2. **Create and Activate a Virtual Environment:**

    * Navigate into the project directory
      cd demoApp

    * Create a virtual environment:
      python -m venv venv

    * Activate the virtual environment:
      Windows: source venv\Scripts\activate
      macOS: source venv/bin/activate

3. **Install the dependencies**

      * pip install -r requirements.txt

4. **Configure the Application:**

    * Edit the demoApp/settings/settings.py file to set your Flask app configurations (e.g., SECRET_KEY, SQLALCHEMY_DATABASE_URI, etc.)

5. **Run the Application:**
  
    * Run the application using the following command:
      python run_app.py

6. **Access the Application:**

    * Open the web browser and navigate to http://127.0.0.1:5000/ to access the application
