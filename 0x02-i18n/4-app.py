#!/usr/bin/env python3
"""
Flask app with Babel integration for internationalization
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

class Config:
    """
    Configuration class for Flask application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages.
    Returns:
        The best match language code.
    """
    # Check if locale parameter is present in the request
    if 'locale' in request.args:
        requested_locale = request.args['locale']
        # Check if the requested locale is in the list of supported languages
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale
    
    # If locale parameter is not present or if it's not a supported locale, fallback to previous behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Route for the index page.
    Returns:
        The rendered HTML for the index page.
    """
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(debug=True)
