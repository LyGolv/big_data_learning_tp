# Use the official Python image as a parent image
FROM python:3.9

# Create a directory named "myapp"
RUN mkdir /app

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port your application will run on
EXPOSE 5000

# Define the command to run your application
CMD ["python", "main.py"]
