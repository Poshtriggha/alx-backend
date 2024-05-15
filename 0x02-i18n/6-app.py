from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

app = Flask(__name__)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """Get user information based on user ID."""
    return users.get(int(user_id))

def get_locale():
    """Determine the best match for supported languages."""
    # Check if locale parameter is present in the URL parameters
    if 'locale' in request.args:
        requested_locale = request.args['locale']
        # Check if the requested locale is in the list of supported languages
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale
    
    # Check if user is logged in and their preferred locale is supported
    if hasattr(g, 'user') and g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Fallback to request header
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    if best_match:
        return best_match

    # Fallback to default locale
    return app.config['BABEL_DEFAULT_LOCALE']

@app.before_request
def before_request():
    """Set user information as a global variable."""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id) if user_id else None

@app.route('/')
def index():
    """Route for the index page."""
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(debug=True)
