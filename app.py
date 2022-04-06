<<<<<<< HEAD
from flask import Flask, url_for, render_template, request
=======
from flask import Flask, render_template
>>>>>>> 0313cbfb285287374efb01cc19d37e82a361a767

app = Flask(__name__)

@app.route('/')
<<<<<<< HEAD
def welcome():
=======
def index() :
>>>>>>> 0313cbfb285287374efb01cc19d37e82a361a767
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)