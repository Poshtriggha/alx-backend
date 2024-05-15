from flask import Flask, render_template, request, g
from flask_babel import Babel, _, lazy_gettext as _l
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

def get_timezone():
    """Determine the best match for supported timezones."""
    # Check if timezone parameter is present in the URL parameters
    if 'timezone' in request.args:
        requested_timezone = request.args['timezone']
        # Validate that the timezone is valid
        try:
            pytz.timezone(requested_timezone)
            return requested_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    
    # Check if user is logged in and their preferred timezone is supported
    if hasattr(g, 'user') and g.user and g.user['timezone']:
        # Validate that the timezone is valid
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Fallback to UTC
    return 'UTC'

@app.before_request
def before_request():
    """Set user information as a global variable."""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id) if user_id else None

@app.route('/')
def index():
    """Route for the index page."""
    return render_template('7-index.html')

if __name__ == '__main__':
    app.run(debug=True)
