# Use the official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install required Python packages
RUN pip install -r requirements.txt --default-timeout=100 future

# Copy everything to the container's working directory
COPY . .

# Expose the port that Chainlit will run on
ENV HOST=0.0.0.0
ENV LISTEN_PORT 8000
EXPOSE 8000

# Command to run your Streamlit application
CMD ["chainlit", "run", "model.py", "-w"]
