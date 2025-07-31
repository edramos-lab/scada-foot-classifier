import cv2, zmq, base64
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: continue
    _, buffer = cv2.imencode('.jpg', frame)
    socket.send(base64.b64encode(buffer))
