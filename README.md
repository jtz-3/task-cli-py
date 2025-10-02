# task-cli-py
A simple task manager CLI tool written in Python.

Stores tasks in a JSON file, with the user able to:
    - Add, Update, and Delete tasks
    - Mark a task as in progress or done
    - List all tasks (including filtering by done/not done/in progress)

TASK PROPERTIES:
    id: A unique identifier for the task
    description: A short description of the task
    status: The status of the task (todo, in-progress, done)
    createdAt: The date and time when the task was created
    updatedAt: The date and time when the task was last updated

COMMAND USAGE:
    task-cli.py add "Description"
    task-cli.py update ID "New description"
    task-cli.py mark-in-progress ID
    task-cli.py mark-done ID
    task-cli.py list
    task-cli.py list done
    task-cli.py list todo
    task-cli.py list in-progress
