from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/health')
def r2_health():
    return jsonify({'Status': '2nd is Up'})


if __name__ == "__main__":
    app.run(debug=True, port=9002)
