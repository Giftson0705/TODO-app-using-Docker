# # Base Image
# FROM python:3.11-slim

# # Set working directory
# WORKDIR /app

# # Install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy project files
# COPY . .

# # Collect static files
# RUN python manage.py collectstatic --noinput

# # Expose port (Render will set $PORT)
# EXPOSE 8000

# # Command to run the app
# CMD gunicorn todoproject.wsgi:application --bind 0.0.0.0:8000


# Use Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start server with Gunicorn
CMD ["gunicorn", "todoproject.wsgi:application", "--bind", "0.0.0.0:8000"]
