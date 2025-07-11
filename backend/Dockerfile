# ✅ Base Python image
FROM python:3.10-slim

# ✅ Set work directory inside container
WORKDIR /app

# ✅ Copy dependency list first for caching
COPY requirements.txt .

# ✅ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy the rest of the backend code
COPY . .

# ✅ Copy .env file if needed inside container (optional if it's in repo)
# COPY .env .env

# ✅ Expose FastAPI default port
EXPOSE 8000

# ✅ Start FastAPI server using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
