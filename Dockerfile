FROM python:3.6-buster
WORKDIR /app
ADD . .
RUN apt-get -y update && apt-get -y install python3-pip python3-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python3", "test_dialog.py"]