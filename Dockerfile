# Base image Python
FROM python:3.14-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        gcc \
        python3-dev \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements/base.txt requirements/base.txt
RUN pip install --upgrade pip \
    && pip install -r requirements/base.txt

# Copy project
COPY . .

# Expose port
EXPOSE 8000

# Jalankan Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
