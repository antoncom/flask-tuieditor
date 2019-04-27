# Flask-TuiEditor

Flask extension for [Tui-Editor](https://github.com/nhn/tui.editor)

## Quick start

> NOTE:
This is early alpha version. It provides simple integration Tui-Editor to your Flask application. See "example" folder to get it worked.

1. pip install https://github.com/antoncom/flask-tuieditor/archive/master.zip
2. Use example/simple/templates/index.html as an example for template editing.
3. Use the code example below:

```
from flask import Flask, render_template
from flask_tuieditor import TuiEditor

app = Flask(__name__)

TuiEditor(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
```

## Special thanks

- It's inspired from [Flask-SimpleMDE](https://github.com/pyx/flask-simplemde). Thank you to [Philip Xu](https://github.com/pyx).