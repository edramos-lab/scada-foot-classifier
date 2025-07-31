FROM nvcr.io/nvidia/l4t-pytorch:r35.3.1-pth2.0-py3

RUN apt-get update && apt-get install -y libsqlite3-dev python3-pip
RUN pip install pyzmq opencv-python numpy torch torchvision

COPY infer_store.py foot_model.pt ./

CMD ["python3", "infer_store.py"]
