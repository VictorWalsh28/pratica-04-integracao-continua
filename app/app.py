from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.get("/health-check")
def health_check():
    return jsonify({"status": "ok"}), 200


@app.get("/hello")
def hello():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    return jsonify({"message": f"Hello, {name}!"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
