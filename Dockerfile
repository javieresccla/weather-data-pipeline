FROM python:3.12-slim

# Prevents python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 
# Forces python to flush output immediately
ENV PYTHONUNBUFFERED=1

# Creates a directory for the app 
WORKDIR /app

# Copies the requirements file to the working directory before the rest  of the code 
COPY requirements.txt .

# Installing dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copies the rest of the code to the working directory
COPY . .

# Default command to run the application, will be overridden by docker-compose
CMD ["python", "-m", "src.extraction.main"]