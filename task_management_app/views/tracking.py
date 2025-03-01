# Tracking routes
# views/tracking.py
from flask import Blueprint, render_template

tracking_bp = Blueprint('tracking', __name__)

@tracking_bp.route('/')
def track_tasks():
    # Placeholder for tracking logic
    return render_template('tracking/track.html')