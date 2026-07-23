from flask import Flask
import os

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "1.0.0")

@app.route("/")
def home():
    return f"Bonjour, ici l'application GitOps de Sada Bousso ! (version {VERSION})\n"

@app.route("/healthz")
def healthz():
    return "OK\n", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
