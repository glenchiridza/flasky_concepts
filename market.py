from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/market/')
def market_page():
    items = [
        {'id':1,'name':'phone','barcode':'2342234242','price':600},
        {'id':2,'name':'tablet','barcode':'236366f433','price':700},
        {'id':3,'name':'laptop','barcode':'0987383ghbb','price':1800},
        {'id':4,'name':'keyboard','barcode':'32gf6674fg','price':800},
    ]
    return render_template('market.html',items=items)


# if __name__ == "__main__":
#     app.run(debug=True,host='127.0.0.1',port=8080)