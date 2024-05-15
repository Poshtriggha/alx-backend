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

@app.before_request
def before_request():
    """Set user information as a global variable."""
    user_id = request.args.get('login_as')
    g.user = get_user(user_id) if user_id else None

@app.route('/')
def index():
    """Route for the index page."""
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(debug=True)
