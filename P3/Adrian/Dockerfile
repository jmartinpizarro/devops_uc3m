# Build stage
FROM python:3.11-slim as builder

WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --user --no-cache-dir -e .

# Production stage
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Add to PATH
ENV PATH=/root/.local/bin:$PATH

# Copy application code
COPY app/ ./app/

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]