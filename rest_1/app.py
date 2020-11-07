from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/health')
def r1_health():
    return jsonify({'Status': '1st is Up'})


if __name__ == "__main__":
    app.run(debug=True, port=9001)
