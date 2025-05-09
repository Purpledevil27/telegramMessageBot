# Dockerfile

# Use Python 3.13 Alpine as the base image for a lightweight container
FROM python:3.13-alpine as builder

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install dependencies without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Use a multi-stage build to reduce the final image size
FROM python:3.13-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

# Copy the application code to the container
COPY . .

# Set the default command to run the bot
CMD ["python", "forward_bot.py"]
