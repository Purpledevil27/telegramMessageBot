FROM python:3.13-alpine

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy bot code
COPY . .

# Run the forward bot
CMD ["python", "forward_bot.py"]
