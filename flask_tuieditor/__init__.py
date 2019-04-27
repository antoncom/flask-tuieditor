
from flask import Blueprint, Markup, current_app, url_for

__version__ = '0.0.1'
__all__ = ['TuiEditor']

JS = [
    'tui-editor-Editor-full.min.js'
]

JS_LINK_TEMPLATE = '<script src="{}"></script>\n'
CSS_LINK_TEMPLATE = '<link rel="stylesheet" href="{}"></link>\n'

CSS = [
    'codemirror.css',
    'highlight.min.css',
    'tui-editor-contents.min.css',
    'tui-editor.min.css'
]

JS_LOAD = """
<script>
    var editor = new tui.Editor({
        el: document.querySelector('#editSection'),
        initialEditType: 'markdown',
        previewStyle: 'vertical',
        height: '300px'
    });
</script>
"""

EXTENSION = "tuieditor"
STATIC_ENDPOINT = EXTENSION + ".static"


class TuiEditor(object):
    """
    Flask-TuiEditor extension
    provides links to TuiEditor's static assets
    """

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Create and register Blueprint with the Flasj application
        :param app:
            Flask application instance
        """

        tuieditor = Blueprint(
            EXTENSION,
            __name__,
            static_folder='static',
            static_url_path=app.static_url_path + "/" + EXTENSION
        )

        app.register_blueprint(tuieditor)

        if not hasattr(app, 'extensions'):
            app.extensions = {}

        app.extensions[EXTENSION] = self
        app.context_processor(lambda: {EXTENSION: self})

    @property
    def css(self):
        """ Property that will be rendered as :code: '<link>' tags for css"""
        code = ''
        for link in CSS:
            code += ''.join(CSS_LINK_TEMPLATE.format(
                url_for(STATIC_ENDPOINT, filename=link)
            ))
        return Markup(code)

    @property
    def js(self):
        """ Property that will be rendered as :code: '<script>' tags for js"""
        code = ''
        for link in JS:
            print(link)
            code += ''.join(JS_LINK_TEMPLATE.format(
                url_for(STATIC_ENDPOINT, filename=link)
            ))
        return Markup(code)

    @property
    def load(self):
        """ Property that will be rendered as javascript loading code"""
        code = JS_LOAD

        return Markup(code)
