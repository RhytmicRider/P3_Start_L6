from django.shortcuts import render
from flask import Flask, render_template

uitgenodigde = ["Ik"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/over")
def over():
    return render_template("over.html")
@app.route("/uitnodiging/<naam>")
def uitnodiging(naam):
    if naam in uitgenodigde:
        return render_template(
            "uitgenodiging.html",
                                naam=naam,
            locatie = "70.974952, 3.259998",
            datum= "19 oktober 1845"


        )
    else:
        return render_template("uitgenodigd.html",
                                datum= "Nope",
                                locatie= "YOU'RE MOM")


if __name__ == "__main__":
   app.run(debug=True)