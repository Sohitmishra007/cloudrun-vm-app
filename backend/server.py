from flask import Flask
app = Flask(__name__)

@app.route("/data")
def send_data():
    return "Hello from the VM backend!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

