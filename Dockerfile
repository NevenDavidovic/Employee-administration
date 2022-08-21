FROM python:3.8.13-alpine
WORKDIR /PIS
ADD . /PIS
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]