FROM docker.io/python:3.10

WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . ./

CMD ["uvicorn", "--host", "0.0.0.0", "app:app"]
