# Task creation routes
# views/tasks.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Task, db

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def list_tasks():
    tasks = Task.query.all()
    return render_template('tasks/list.html', tasks=tasks)

@tasks_bp.route('/<int:task_id>')
def task_detail(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('tasks/detail.html', task=task)

@tasks_bp.route('/create', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        status = request.form.get('status', 'Pending')
        priority = request.form.get('priority', 'Medium')
        due_date = request.form.get('due_date')
        
        new_task = Task(
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('tasks.list_tasks'))
    return render_template('tasks/form.html')

@tasks_bp.route('/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        task.status = request.form.get('status')
        task.priority = request.form.get('priority')
        task.due_date = request.form.get('due_date')
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('tasks.task_detail', task_id=task.id))
    return render_template('tasks/form.html', task=task)

@tasks_bp.route('/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('tasks.list_tasks'))