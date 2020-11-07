from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def r1_health():
    return jsonify({'Status': '1st is Up'})


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8001)
