FROM python:3.6
WORKDIR /usr/scripts/herbie
RUN apt-get update
RUN pip install pyrealsense2
COPY pyrealsenseTest.py .
CMD ["python", "./pyrealsenseTest.py"]