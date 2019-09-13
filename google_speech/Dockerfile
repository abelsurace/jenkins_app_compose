# Use an official Python runtime as a parent image
# **Build image**  docker build --tag=google_speech:v0.0.1 .
# **Run container ** docker run -it -d --name google_speech --group-add audio --privileged -p 5600:5600 google_speech:v0.0.1
FROM python:3.7-slim

# Set the working directory to /Jenkins_status
WORKDIR /pyTalk

# Copy the current directory contents into the container at /app
COPY pyTalk /pyTalk
COPY requirements.txt /pyTalk

#install multiple packages 
RUN apt-get update && apt-get install -y  --allow-unauthenticated\
    iputils-ping \
    vim \
    net-tools \
    sox \
    libsox-fmt-mp3 \	
    alsa-utils \
	libgl1-mesa-dri \
	libgl1-mesa-glx \
	libpulse0 


# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5600

# Run app.py when the container launches
CMD ["python", "pyTalk.py"]
