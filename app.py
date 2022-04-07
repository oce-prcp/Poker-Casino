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
    
    session['erreur_age'] = False
    if sexe.lower() in sexes:
        if age < 18:
            session['erreur_age'] = "Vous n'avez pas l'âge requis"
            return render_template('index.html')
        elif age >= 18:
            session['bankroll'] = request.form['bankroll']
            return redirect(url_for('play'))

#------------------------------PAGE PLAY---------------------------

@app.route('/play',methods=['POST','GET'])
def play():
    return render_template('play.html')

#------------------------------LOGOUT---------------------------
""" 
@app.route('/logout', methods=['GET'])
def logout():
    if session['id'] != None:
        session['id'] = None
        return redirect('/', 302)
    else:
        return redirect('/', 302)
"""


if __name__ == '__main__':
    app.run(debug=True)