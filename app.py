
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask deployed on Render 2302600020! dina mangunsong update!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
