import os

def create_directory(path):
    """Create a directory if it doesn’t exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")
    else:
        print(f"Directory already exists: {path}")

def create_file(path, content=''):
    """Create a file with optional content if it doesn’t exist."""
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write(content)
        print(f"Created file: {path}")
    else:
        print(f"File already exists: {path}")

# Define the project structure
directories = [
    'task_management_app',
    'task_management_app/views',
    'task_management_app/templates',
    'task_management_app/templates/tasks',
    'task_management_app/templates/assignments',
    'task_management_app/templates/prioritization',
    'task_management_app/templates/tracking',
    'task_management_app/templates/reporting',
    'task_management_app/static',
    'task_management_app/static/css',
    'task_management_app/utils',
]

files = {
    'task_management_app/app.py': '# Main Flask application\n',
    'task_management_app/requirements.txt': 'Flask>=2.0.0\n',
    'task_management_app/config.py': '# Configuration settings\n',
    'task_management_app/models.py': '# Data models\n',
    'task_management_app/views/__init__.py': '# views package\n',
    'task_management_app/views/tasks.py': '# Task creation routes\n',
    'task_management_app/views/assignments.py': '# Assignment routes\n',
    'task_management_app/views/prioritization.py': '# Prioritization routes\n',
    'task_management_app/views/tracking.py': '# Tracking routes\n',
    'task_management_app/views/reporting.py': '# Reporting routes\n',
    'task_management_app/templates/base.html': '<!-- Base template -->\n',
    'task_management_app/templates/tasks/list.html': '<!-- Task list -->\n',
    'task_management_app/templates/tasks/detail.html': '<!-- Task details -->\n',
    'task_management_app/templates/tasks/form.html': '<!-- Task form -->\n',
    'task_management_app/templates/assignments/form.html': '<!-- Assignment form -->\n',
    'task_management_app/templates/prioritization/prioritize.html': '<!-- Prioritization page -->\n',
    'task_management_app/templates/tracking/track.html': '<!-- Tracking page -->\n',
    'task_management_app/templates/reporting/report.html': '<!-- Reporting page -->\n',
    'task_management_app/static/css/style.css': '/* CSS styles */\n',
    'task_management_app/utils/__init__.py': '# utils package\n',
    'task_management_app/utils/singleton.py': '# Singleton pattern implementation\n',
    'task_management_app/utils/observers.py': '# Observer pattern implementation\n',
    'task_management_app/utils/strategies.py': '# Strategy pattern implementation\n',
}

# Create directories
for dir_path in directories:
    create_directory(dir_path)

# Create files
for file_path, content in files.items():
    create_file(file_path, content)

print("File structure created successfully!")