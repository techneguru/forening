from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)
API_BASE = os.getenv("API_BASE", "http://noco:8080/api/v1/db/data/v1/breforening")
API_KEY = os.getenv("API_KEY", "default_api_key")

@app.route('/api/news', methods=['GET'])
def get_news():
    headers = {"xc-auth": API_KEY}
   try:
        response = requests.get(f"{API_BASE}/news", headers=headers)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": "Failed to fetch news"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)