from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hello from the greeting microservice!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
