# task-cli-py
A simple task manager CLI tool written in Python.

Stores tasks in a JSON file, with the user able to:
    - Add, Update, and Delete tasks
    - Mark a task as in progress or done
    - List all tasks (including filtering by done/not done/in progress)

TASK PROPERTIES: <br>
    &emsp; id: A unique identifier for the task<br>
    &emsp; description: A short description of the task<br>
    &emsp; status: The status of the task (todo, in-progress, done)<br>
    &emsp; createdAt: The date and time when the task was created<br>
    &emsp; updatedAt: The date and time when the task was last updated<br>

COMMAND USAGE: <br>
    &emsp; task-cli.py add "Description"<br>
    &emsp; task-cli.py update ID "New description"<br>
    &emsp; task-cli.py mark-todo ID<br>
    &emsp; task-cli.py mark-in-progress ID<br>
    &emsp; task-cli.py mark-done ID<br>
    &emsp; task-cli.py list all<br>
    &emsp; task-cli.py list done<br>
    &emsp; task-cli.py list todo<br>
    &emsp; task-cli.py list in-progress<br>
