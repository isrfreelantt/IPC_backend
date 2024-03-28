FROM python:3.12

ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the backend source code into the container
COPY . /app

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0"]