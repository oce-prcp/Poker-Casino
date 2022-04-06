from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    return "Hello world."


@app.route('/hello/<name>', methods=['GET'])
def hello(name): ## ça du coup c'est un exemple de route qui prend des arguments en get ok?
    return name # je créer une route qui n'accepte que la méthode GET et qui en gros prend en parametre get unnom et j'afficeh l parametre look


@app.route('/login', methods=['POST'])
def login():
    return request.POST.get('username') # donc là si on va sur la route en get il detecte que y'a pas de route par conte si j'envois une requetes de type post tu vas voir
    
if __name__ == '__main__': # ca j'ai pas compris att c normaé oki
    app.run() 