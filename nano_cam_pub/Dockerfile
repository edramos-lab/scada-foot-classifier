FROM nvcr.io/nvidia/l4t-base:v2.0.2-r32.7.1

RUN apt-get update && apt-get install -y python3 python3-pip libopencv-dev python3-opencv
RUN pip3 install pyzmq numpy

COPY cam_pub.py /cam_pub.py

CMD ["python3", "/cam_pub.py"]
