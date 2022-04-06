from crypt import methods
from flask import Flask, url_for, render_template, request, session
from main import *
app = Flask(__name__)
app.secret_key="secret_key_sexe"


@app.route('/',methods=['GET'])
def accueil():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index() :
    sexe = request.form['sexe']

    if sexe.lower() == "homme":
        session["message"] = "Vous êtes un homme"
        return render_template('index.html')    

    elif sexe.lower() == "femme":
        session["message"] = "Vous êtes une femme"
        return render_template('index.html')
    



if __name__ == '__main__':
    app.run(debug=True)