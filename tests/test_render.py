import flask

from flask_tuieditor import TuiEditor

TEMPLATE = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Flask-TuiEditor example</title>
    {{ tuieditor.css }}
    {{ tuieditor.js }}
  </head>
  <body>
    {{ tuieditor.load }}
    {{ tuieditor.load_id("editor") }}
  </body>
</html>
"""

STATIC_CSS = '/static/tuieditor/tuieditor.min.css'
STATIC_JS = '/static/tuieditor/tuieditor.min.js'
