from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('Home.html')
@app.route('/market')
def market_page():[
    {'id':1,'name':'phone','barcode':'45614264978241','price':5000},
    {'id':2, 'name':'laptop', 'barcode': '21435746778241', 'price': 9000},
    {'id':3, 'name':'keyboard', 'barcode': '45614245142323', 'price': 3000}
]
    return render_template('market.html',items=items)