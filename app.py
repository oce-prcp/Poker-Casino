from flask import Flask, redirect, url_for, render_template, request, session
from main import premier_tirage
import random
app = Flask(__name__)
app.secret_key="secret_key_sexe"


@app.route('/',methods=['GET'])
def accueil():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index() :
    sexe = request.form['sexe']
    age = int(request.form['age'])

    sexes = ["femme", "homme"]
    if sexe.lower() in sexes:
        if age >= 18:
            random_id = random.randint(10000, 20000)
            session['id'] = random_id
            return redirect('/bankroll', 302)
        else:
             return render_template('index.html', message="Vous n'êtes pas majeur")
    else:
        return render_template('index.html', message="Les autres genre ne sont pas acceptés")


@app.route('/bankroll',methods=['GET', 'POST'])
def bankroll():
    confirmation = 0
    if request.method == "POST":
        bankroll = int(request.form.get('bankroll'))
        mise = int(request.form.get('mise'))
        while confirmation != 1:
            if bankroll <= 0 or mise <= 0:
                 return render_template('bankroll.html', message="Veuillez inserer une valeur superieur a 0")
            elif bankroll >= 1 and mise >= 1:
                confirmation += 1
                return redirect('/play', 302)
        
        if session['id'] == None:
            return redirect('/', 302)
    
    return render_template('bankroll.html')

@app.route('/play',methods=['GET','POST'])

def play():
    return render_template('play.html')


@app.route('/logout', methods=['GET'])
def logout():
    if session['id'] != None:
        session['id'] = None
        return redirect('/', 302)
    else:
        return redirect('/', 302)



if __name__ == '__main__':
    app.run(debug=True)
    
