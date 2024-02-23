FROM python:3.11

RUN mkdir working
RUN mkdir yolov3
COPY ./yolov3 ./yolov3

RUN mkdir templates

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD ./templates ./templates
ADD *.py ./


EXPOSE 8080
CMD ["python", "./server.py"] 
