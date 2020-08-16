from flask import Flask, render_template,request

app = Flask("__main__")

@app.route('/')
def index():
    return render_template('index.html',token='Welcome to nba stats')




app.run(debug=True)