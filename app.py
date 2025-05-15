from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.errorhandler(400)
def bad_request(error):
    return "Bad request", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
