from flask import Flask, send_file
import sqlite3, io

app = Flask(__name__)

@app.route("/")
def dashboard():
    return "Foot Diagnostics Running"

@app.route("/latest")
def latest():
    db = sqlite3.connect("foot_diagnostics.db")
    c = db.cursor()
    c.execute("SELECT foot_type, image FROM foot_data ORDER BY timestamp DESC LIMIT 1")
    ft, img = c.fetchone()
    return send_file(io.BytesIO(img), mimetype='image/jpeg', as_attachment=False, download_name=f"{ft}.jpg")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
