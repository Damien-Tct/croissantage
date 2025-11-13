#! /usr/bin/env python3

from flask import Flask, render_template, request
from datetime import datetime, timedelta


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "Aeniep1IyieChah8cah9ailee$chile0naJiel2eiD4iquah3y"

class CroissantForm(FlaskForm):
    nom = StringField("La personne croissantée", validators=[DataRequired()])
    croissant = SelectField(
        "Choisis ta viennoiserie 🥐",
        choices=[
            ('croissant', 'Croissant'),
            ('chocolatine', 'Chocolatine')
        ],
        validators=[DataRequired()])
    submit = SubmitField("Croissanter")


@app.route('/',methods=['GET', 'POST'])

def index():
    if request.method == "GET":
        form = CroissantForm()

    # Génère une date aléatoire dans les 30 prochains jours
        request_type = type(request)
    
        return render_template("index.html", request=request, form = form)

    if request.method == "POST":
        nom = request.form.get("nom")
        croissant = request.form.get("croissant")

        return render_template("index.html", request=request, nom=nom, croissant=croissant)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

