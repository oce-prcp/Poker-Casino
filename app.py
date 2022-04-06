from flask import Flask, url_for, render_template, request
#from main.py import Main
#from Main import premier_tirage
app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def gfg():
    confirm = 0
    if request.method == "POST":
        age = request.form.get("age")
        
        while confirm != 1:
            if int(age) >= 18:
                return "Vous êtes majeur, passez."
           
            else:
                return "Vous êtes mineur. Dégagez"
    return render_template('age_confirm.html')

@app.route('/index.html')
def index() :
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
