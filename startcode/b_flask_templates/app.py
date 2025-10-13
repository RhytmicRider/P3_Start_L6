from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hallo wereld!</h1><p>Dit is mijn eerste Flask app</p>"

@app.route("/over")
def over():
    return "<h1>Over</h1><p>Dit is een testwebsite!</p>"

@app.route("/gebruiker/<naam>")
def gebruiker_profiel(naam):
    return f"<h1>Welkom {naam}!</h1><p>Dit is jouw profiel</p>"

if __name__ == "__main__":
   app.run(debug=True)