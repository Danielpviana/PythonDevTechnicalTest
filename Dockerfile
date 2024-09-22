# Use the official Python image from the Docker Hub
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the necessary packages
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "-m", "flask", "--app", "./app/app.py", "run", "--host=0.0.0.0"]
