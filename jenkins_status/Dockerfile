# Use an official Python runtime as a parent image
#  **Build image***  docker build --tag=jenkins_status:v0.0.1 .
#  **Run Container**   docker run -name jenkins_status jenkins_status:v0.0.1
FROM python:2.7-slim

# Set the working directory to /Jenkins_status
WORKDIR /Jenkins-status

# Copy the current directory contents into the container at /app
COPY Jenkins-status /Jenkins-status
COPY requirements.txt /Jenkins-status

#install multiple packages 
RUN apt-get update && apt-get install -y  --allow-unauthenticated\
    iputils-ping \
    vim \
    net-tools

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "python/jenkins_indicator.py"]
