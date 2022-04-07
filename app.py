from flask import Flask, redirect, url_for, render_template, request, session
from main import *
app = Flask(__name__)
app.secret_key="secret_key_sexe"

#--------------------------------PAGE INDEX--------------------------------

@app.route('/')
def accueil():
    return render_template('index.html')


@app.route('/', methods=['POST','GET'])
def index():
    sexe = request.form['sexe']
    age = int(request.form['age'])
    sexes = ["femme", "homme"]
    
    session['erreur_index'] = False
    
    if sexe.lower() in sexes:
        if age < 18:
            session['erreur_index'] = "Vous n'avez pas l'âge requis"
            return render_template('index.html')

        elif age >= 18:
            session['bankroll'] = request.form['bankroll']

            if int(session['bankroll']) >= 10:
                session['erreur_index'] = "Veuillez saisir une bankroll supérieure à 10"
                return redirect(url_for('display'))

#------------------------------PAGE PLAY---------------------------
@app.route('/play')
def display():
    return render_template('play.html')

@app.route('/play', methods=['POST','GET'])
def play():
    if "mise" in request.form:

        session['mise'] = int(request.form['mise'])
        if session['mise'] > int(session['bankroll']):
            session['erreur_mise'] = "Vous ne pouvez pas miser plus que votre bankroll"
            return render_template('play.html')
    return render_template('play.html')

#---------------------SUPPRESSION CACHE (ALLER SUR 127.0.0.1/a)--------------------

@app.route('/a')
def a():
    session.clear()
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)