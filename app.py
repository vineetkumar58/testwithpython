from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Python Auto Deploy Works but this is 2nd commit!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

