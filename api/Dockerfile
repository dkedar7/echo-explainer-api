FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app