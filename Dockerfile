# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

RUN pip install mysql-connector-python
RUN pip install SQLAlchemy

# Setting the working directory in the container
WORKDIR /app

# Install system packages required for building Python packages that depend on MySQL
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential libmariadb-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*


# Copying the requirements file into the container at /demoApp
COPY requirements.txt /app/

# Installing any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copying the rest of the application code into the container at /app
COPY . /app/

# Expose port 5000 for Flask app
EXPOSE 5000

# Specify the command to run your application
CMD ["python", "controller.py"]
