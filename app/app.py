from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/health-check")
def health_check():
    return jsonify({"status": "ok"}), 200


@app.get("/hello")
def hello():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    return jsonify({"message": f"Hello, {name}!"}), 200
