# Use lightweight Python image
FROM python:3.12-slim

# Prevent Python from buffering output
ENV PYTHONUNBUFFERED=1

# Working directory inside container
WORKDIR /app

# Copy dependency file first (better Docker caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]