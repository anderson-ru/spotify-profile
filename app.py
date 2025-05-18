from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Spotify backend работает!"

@app.route("/callback")
def callback():
    code = request.args.get("code")
    return f"Получен код: {code}"
