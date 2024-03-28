FROM python:3.12

ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

RUN  apk update \
	&& apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
	&& pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["sh", "entrypoint.sh"]