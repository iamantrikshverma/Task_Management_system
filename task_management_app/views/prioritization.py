# Prioritization routes
# views/prioritization.py
from flask import Blueprint, render_template

prioritization_bp = Blueprint('prioritization', __name__)

@prioritization_bp.route('/')
def prioritize_tasks():
    # Placeholder for prioritization logic
    return render_template('prioritization/prioritize.html')