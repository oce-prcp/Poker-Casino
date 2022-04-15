from flask import Flask, redirect, url_for, render_template, request, session
from main import premier_tirage, deuxieme_tirage
import random
from main import *
app = Flask(__name__)
app.secret_key="secret_key_sexe"

#--------------------------------PAGE INDEX--------------------------------

@app.route('/')
def accueil():
    return render_template('index.html')


@app.route('/', methods=['POST','GET'])
def index():
    session.clear()
    sexe = request.form['sexe']
    age = int(request.form['age'])
    session['Bankroll'] = int(request.form.get('bankroll'))

    sexes = ["femme", "homme"]
    erreur_index = ""
    session['erreur_index'] = erreur_index
    
    if sexe.lower() in sexes:
        if age >= 18:
            if session['Bankroll'] >= 1:
                return redirect('/play', 302)
            else:
                return render_template('index.html', erreur_index="Faites pas le clochard")
        else:
            return render_template('index.html', erreur_index="Vous n'êtes pas majeur")
    else:
        return render_template('index.html', erreur_index="Les autres genres ne sont pas acceptés")

#------------------------------PAGE PLAY---------------------------
@app.route('/play',methods=['GET','POST'])

def play():
    session['deck'] = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
    
    if request.method == "POST":
        session['bet'] = int(request.form.get('bet'))

        if session['bet'] <= session['Bankroll']:
            session['Bankroll'] = session['Bankroll'] - session['bet']

            tirage1, deck_apres_1er_tirage = premier_tirage(session['deck'])
            session['tirage1'] = tirage1
            session['deck_apres_1er_tirage'] = deck_apres_1er_tirage

            return redirect(url_for('play_2'))

        else:
            session['erreur_mise'] = "Vous ne pouvez miser ce que vous n'avez pas."
            session.pop('bet')
            return render_template('play.html')

    return render_template('play.html')        





@app.route('/play_2', methods=['GET','POST'])
def play_2():
    if request.method == "POST":
        session['i'] = request.form.getlist('i')
        return redirect(url_for('deuxieme_tirage'))

    return render_template('play_2.html')





@app.route('/deuxieme_tirage', methods=['GET','POST'])
def deuxieme_tirage(): 
    carteAtirer = 5 - len(session['i'])
    print(session['i'])
    tiragedeux = random.sample(session['deck'], carteAtirer)
    session['tirageFinal'] = session['i'] + tiragedeux
    
    print(session['tirageFinal'])

    valeur, couleur = decomp(session['tirageFinal'])
    session['valeur'] = valeur
    session['couleur'] = couleur
    print(session['valeur'])
    print(session['couleur'])

    gain, result = combinaisons(session['tirageFinal'],session['bet'])
    session['gain'] = gain
    session['result'] = result
    print(session['gain'])
    print(session['result'])

    session['Bankroll'] = session['Bankroll'] + session['gain']
    if session['Bankroll'] <= 0 :
        return redirect(url_for('Lose'))
    return render_template('deuxieme_tirage.html')

@app.route('/Lose')
def Lose():
    return render_template('Lose.html')

@app.route('/a')
def a():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
