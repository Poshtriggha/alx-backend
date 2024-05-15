from flask import Flask, render_template, request, g
from flask_babel import Babel, _, lazy_gettext as _l
import pytz
from datetime import datetime

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
    # Same as before

def get_current_time(timezone):
    """Get the current time in the specified timezone."""
    try:
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz).strftime('%b %d, %Y, %I:%M:%S %p')
        return current_time
    except pytz.exceptions.UnknownTimeZoneError:
        return None

@app.before_request
def before_request():
    """Set user information as a global variable."""
    # Same as before

@app.route('/')
def index():
    """Route for the index page."""
    current_time = get_current_time(get_timezone())
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
