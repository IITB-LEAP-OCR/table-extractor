FROM python:3.10.5

# Set working directory inside container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6

# Add Python dependencies
ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source files and directories
ADD infer.py .
ADD ./tables/ ./tables/
ADD ./uploads/ ./uploads/
ADD main.py .  

# Expose FastAPI default port
EXPOSE 8000

# Run FastAPI app instead of infer.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]