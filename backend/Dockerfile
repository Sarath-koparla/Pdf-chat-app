FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# ✅ Add this fix
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

