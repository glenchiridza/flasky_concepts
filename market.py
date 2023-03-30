from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/market')
def market_page():
    return render_template('market.html',item_name='phone')


# if __name__ == "__main__":
#     app.run(debug=True,host='127.0.0.1',port=8080)