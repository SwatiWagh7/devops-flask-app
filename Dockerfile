# 1️⃣ Use lightweight Python image
FROM python:3.10-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy dependency file first (Docker cache optimization)
COPY requirements.txt .

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy application code
COPY app.py .

# 6️⃣ Expose Flask port
EXPOSE 5000

# 7️⃣ Run the application
CMD ["python", "app.py"]

