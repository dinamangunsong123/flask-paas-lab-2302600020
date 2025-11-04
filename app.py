from flask import Flask

app = Flask(name)

@app.route('/')
def home():
    return "Hello from Flask deployed on Render 213510321!"

if name == 'main':
    app.run(host='0.0.0.0', port=5000)