from flask import Flask, render_template
from flask_tuieditor import TuiEditor

app = Flask(__name__)

TuiEditor(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
