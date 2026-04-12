# Use lightweight Python image
FROM python:3.10-slim

<<<<<<< HEAD
# Set working directory
WORKDIR /app

# Copy all project files
COPY . .
=======
# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (needed for some ML libs)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (for caching)
COPY requirements.txt .
>>>>>>> d2213c6 (Initial commit - Deepfake Detection project)

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

<<<<<<< HEAD
=======
# Copy rest of the project
COPY . .

# Create logs directory (IMPORTANT for your assignment)
RUN mkdir -p logs

>>>>>>> d2213c6 (Initial commit - Deepfake Detection project)
# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]