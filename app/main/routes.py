"""Main routes for home page and leaderboard.

This module handles the home page and the leaderboard. The weather widget
is fetched on the frontend via JavaScript (Open‑Meteo) to work on platforms
without outbound network access, such as PythonAnywhere free plan.
"""

from flask import render_template
from app.main import main_bp
from app.models import User


@main_bp.route('/', methods=['GET'])
def home():
    """Render home page with weather widget.

    The weather data is loaded client-side via JavaScript. No server-side
    network calls are performed.

    Returns:
        Rendered home page template.
    """
    return render_template('home.html')


@main_bp.route('/leaderboard')
def leaderboard():
    """Display leaderboard with top users by score.

    Returns:
        Rendered leaderboard template with sorted users.
    """
    # Get top 50 users by score
    top_users = User.query.order_by(User.total_score.desc()).limit(50).all()

    return render_template('leaderboard.html', users=top_users)
