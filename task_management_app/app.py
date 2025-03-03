# Main Flask application
from flask import Flask, redirect, url_for
from config import Config
from models import db
from views.tasks import tasks_bp
from views.assignments import assignments_bp
from views.prioritization import prioritization_bp
from views.tracking import tracking_bp
from views.reporting import reporting_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Register blueprints
app.register_blueprint(tasks_bp, url_prefix='/tasks')
app.register_blueprint(assignments_bp, url_prefix='/assignments')
app.register_blueprint(prioritization_bp, url_prefix='/prioritization')
app.register_blueprint(tracking_bp, url_prefix='/tracking')
app.register_blueprint(reporting_bp, url_prefix='/reporting')

@app.route('/')
def index():
    return redirect(url_for('tasks.list_tasks'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates database and tables if they don’t exist
    app.run(debug=True)