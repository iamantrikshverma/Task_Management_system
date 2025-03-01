# Reporting routes
# views/reporting.py
from flask import Blueprint, render_template

reporting_bp = Blueprint('reporting', __name__)

@reporting_bp.route('/')
def generate_report():
    # Placeholder for reporting logic
    return render_template('reporting/report.html')