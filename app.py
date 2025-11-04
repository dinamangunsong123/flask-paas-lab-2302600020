from flask import Flask

app = Flask(name)

@app.route('/')
def home():
    return "Hello from Flask deployed on Render 2302600020!"

if name == 'main':
    app.run(host='0.0.0.0', port=5000)
