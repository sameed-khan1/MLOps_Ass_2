FROM python:3.10

WORKDIR /app

COPY . .

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]