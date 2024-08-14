from flask import Flask, render_template
from dash_app import create_dash_app

app = Flask(__name__)
dash_app = create_dash_app(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashs')
def dashs():
    return render_template('dashs.html', dash_app_entry=dash_app.index())

if __name__ == '__main__':
    app.run(debug=True)
 