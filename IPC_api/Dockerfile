FROM python:3.12

ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["sh", "entrypoint.sh"]