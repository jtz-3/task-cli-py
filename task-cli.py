#!/usr/bin/python3

# A task manager CLI tool.

"""
    1. Consider adding 'mark-todo'.
    2. Consider only updating file if modifications have been made.
"""

import sys
import json
import datetime

# Retrieve the command
# Valid commands: add, update, delete, mark-in-progress, mark-done, list (all/done/todo/inprogress)
try:
    command = sys.argv[1]
except IndexError:
    print('Error: no command specified.')
    quit()

# Load and deserialize the task file, or create it if it doesn't exist.
# Is this proper use of try/except? Maybe if/else is more appropriate.
try:
    task_file = open('./tasks.json', 'r+')
    tasks = json.load(task_file)
    file_exists = True
except FileNotFoundError:
    tasks = {}
    file_exists = False

# Determine the ID of the next task to be added, as well as the number of CLI args passed.
current_id = len(tasks) + 1
num_args = len(sys.argv)

if command == 'add':
    if num_args == 2:
        print('Error: No task description given.')
    elif num_args > 3:
        print('Error: Only one description can be given. (Enclose description in quotation marks.)')
    else:
        task_desc = str(sys.argv[2])
        if not task_desc in tasks:
            tasks[current_id] = {"description": task_desc,
                                "status": "todo",
                                "createdAt": str(datetime.datetime.today()),
                                "updatedAt": None}
            print('Task added successfully (ID: %s)' % current_id)
        else:
            print('Error: Cannot re-add an existing task.')

elif command == 'update':
    if num_args != 4:
        print('Error: Invalid number of arguments. (Format: task-cli update ID "Description")')
    elif type(sys.argv[3]) != str:
        print('Error: Invalid description passed.')
    elif not sys.argv[2].isdigit() or (int(sys.argv[2]) <= 0 or int(sys.argv[2]) >= current_id):
        print('Error: ID must be a valid integer.')
    else:
        # Update the tasks - since tasks must exist (per above), can just access the tasks dictionary directly.
        tasks[sys.argv[2]]["description"] = sys.argv[3]
        tasks[sys.argv[2]]["updatedAt"] = str(datetime.datetime.today())
        print('Successfully updated task %s.' % sys.argv[2])
        
elif command == 'delete':
    if num_args != 3:
        print('Error: Invalid number of arguments. (Format: task-cli delete ID).')
    elif not sys.argv[2].isdigit() or (int(sys.argv[2]) <= 0 or int(sys.argv[2]) >= current_id):
        print('Error: Invalid ID number.')
    else:
        del tasks[sys.argv[2]]
        print('Successfully deleted task %s.' % sys.argv[2])

# ADD MARK-TODO. Then handle the command selection more elegantly (begins with mark-...)
elif command == 'mark-in-progress' or command == 'mark-done':
    if num_args != 3:
        print('Error: Invalid number of arguments. (Format: task-cli mark-in-progress ID, or ' \
        '      task-cli mark-done ID.)')
    elif not sys.argv[2].isdigit() or (int(sys.argv[2]) <= 0 or int(sys.argv[2]) >= current_id):
        print('Error: Invalid ID number.')
    else:
        # Will set status to 'in-progress' or 'done'
        tasks[sys.argv[2]]['status'] = sys.argv[1][5:]
        print('Task %s successfully marked as %s.' % (sys.argv[2], sys.argv[1][5:]))
elif command == 'list':
    # TODO: Add error handling for when no JSON file exists.
    # TODO: Add handling of arguments for task status (done, todo, in-progress)


    if num_args != 3:
        print('Error: Invalid number of arguments. (Format: task-cli list {all, done, todo, in-progress})')
    else:
        status = sys.argv[2]

        if status not in ('all', 'done', 'todo', 'in-progress'):
            print('Error: Invalid task status supplied. (Must be one of: all, done, todo, in-progress)')
        else:
            if status == 'all':
                task_list = tasks
            else:
                task_list = {}

                # Filter task list by appropriate status.
                for t in tasks.items():
                    if tasks[t[0]]['status'] == status:
                        task_list.update({t[0]: t[1]})

            if len(task_list) != 0:
                print('Listing all tasks in category:', status)
            else:
                print('No tasks found in category "%s"!' % status)

            for tsk in task_list.items():
                print('- ID:', tsk[0])
                print('  - Description:', tsk[1]['description'])
                if status == 'all':
                    print('  - Status:', tsk[1]['status'])
                print('  - Creation date:', tsk[1]['createdAt'])
                print('  - Last updated:', tsk[1]['updatedAt'])
                print('\n')

else:
    print('Error: invalid command specified.')

# Deserialize tasks dictionary into JSON and then write it to the file, creating it if it doesn't exist
if not file_exists:
    task_file = open('tasks.json', 'w')
    print('New file created')
else:
    task_file.seek(0)
    task_file.truncate()

json.dump(tasks, task_file)
task_file.close()