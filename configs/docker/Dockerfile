FROM python:3.9-slim

LABEL maintainer="CyberSec-Arsenal"
LABEL description="Security testing environment"

# Install basic utilities
RUN apt-get update && apt-get install -y \
    nmap \
    netcat \
    curl \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /opt/cybersec-arsenal

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["bash"]
