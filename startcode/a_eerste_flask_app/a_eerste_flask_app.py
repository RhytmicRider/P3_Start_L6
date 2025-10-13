from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hallo wereld!</h1><p>Dit is mijn eerste Flask app</p>"

if __name__ == "__main__":
   app.run(debug=True)