import zmq, base64, sqlite3, torch, cv2
import numpy as np
from datetime import datetime

model = torch.load("foot_model.pt", map_location='cuda')
model.eval()

db = sqlite3.connect("foot_diagnostics.db")
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS foot_data (timestamp TEXT, patient TEXT, foot_type TEXT, image BLOB)")
db.commit()

socket = zmq.Context().socket(zmq.SUB)
socket.connect("tcp://<JETSON_NANO_IP>:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, '')

def preprocess(img):
    img = cv2.resize(img, (224, 224))
    img = img.transpose(2, 0, 1) / 255.0
    return torch.tensor(img).unsqueeze(0).float().to('cuda')

labels = ['Flat', 'Neutral', 'High']

while True:
    data = base64.b64decode(socket.recv())
    arr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    x = preprocess(img)
    with torch.no_grad():
        out = model(x).argmax().item()
    foot_type = labels[out]
    cur.execute("INSERT INTO foot_data VALUES (?, ?, ?, ?)", (datetime.now().isoformat(), "patient001", foot_type, data))
    db.commit()
