# Assignment routes
# views/assignments.py
from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Assignment, Task, User

assignments_bp = Blueprint('assignments', __name__)

@assignments_bp.route('/create', methods=['GET', 'POST'])
def create_assignment():
    tasks = Task.query.all()
    users = User.query.all()
    if request.method == 'POST':
        task_id = request.form['task_id']
        user_id = request.form['user_id']
        new_assignment = Assignment(task_id=task_id, user_id=user_id)
        db.session.add(new_assignment)
        db.session.commit()
        return redirect(url_for('tasks.list_tasks'))
    return render_template('assignments/form.html', tasks=tasks, users=users)