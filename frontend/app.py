from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    response = requests.get("http://10.160.0.2:5000/data")  # Replace later
    return f"Frontend says: {response.text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

