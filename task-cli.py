# A task manager CLI tool.

# NOTE NEXT STEPS HERE.
# NEXT STEPS 10/2/25
"""
    1. Work on mark-in-progress, mark-done commands
    2. Consider adding separate error messages for updating/deleting if no file exists.
"""

import sys
import json
import datetime

# Retrieve the command
# Valid commands: add, update, delete, mark-in-progress, mark-done, list (done/todo/inprogress)
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

# Debug
# print("OLD TASK FILE:")
# for k in tasks.keys():
#     print(k + ": ")
#     print(tasks[k])
# print('\n')

# Consider replacing this with num_tasks and then adding 1 elsewhere (depends on most common usage)
current_id = len(tasks) + 1
num_args = len(sys.argv)

if command == 'add':

    if num_args == 2:
        print('Error: No task name specified.')
    elif num_args > 3:
        print('Error: Only one description can be given. (Enter text in quotation marks.)')
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
    # Errors to be handled:
    # - Invalid number of arguments
    # - Invalid argument types for description (str) and 
    #   - Although it will coerce to string anyway.
    # - Invalid ID provided
    #   - No tasks to update?

    if num_args != 4:
        print('Error: Invalid number of arguments. (Format: task-cli update ID "Description")')
    elif type(sys.argv[3]) != str:
        print('Error: Invalid description passed.')
    elif not sys.argv[2].isdigit() or (int(sys.argv[2]) <= 0 or int(sys.argv[2]) >= current_id):
        print('Error: ID must be a valid integer.')
        print(sys.argv[2], type(sys.argv[2]), current_id)
    else:
        # Update - since tasks must exist, can just access the tasks dictionary.
        tasks[sys.argv[2]]["description"] = sys.argv[3]
        tasks[sys.argv[2]]["updatedAt"] = str(datetime.datetime.today())
        print('Updated successfully')
        
elif command == 'delete':
    # Errors to be handled:
    # - Improper formatting
    #   - task-cli.py delete 1 (2 arguments)
    # - File doesn't exist
    # - No task with that ID exists

    if num_args != 3:
        print('Error: Invalid number of arguments. (Format: task-cli delete ID).')
    elif not sys.argv[2].isdigit() or (int(sys.argv[2]) <= 0 or int(sys.argv[2]) >= current_id):
        print('Error: Invalid ID number.')
    else:
        del tasks[sys.argv[2]]
# NOTE: Maybe mark-in-progress, mark-done can be lumped together. Same structure and basic functionality.
elif command == 'mark-in-progress':
    pass
    # TODO: Throw an error if task does not exist
    # TODO: Throw an error if no file exists
elif command == 'mark-done':
    pass
    # TODO: Throw an error if task does not exist
elif command == 'list':
    pass
    # TODO: Add error handling for when no JSON file exists.
    # TODO: Add handling of arguments for task status (done, todo, in-progress)
else:
    print('Error: invalid command specified.')
    # quit()
    
# TODO: Make script to run as a command without .py extension (use shebang)




# Deserialize tasks dictionary into JSON and then write it to the file, creating it if it doesn't exist
if file_exists:
    task_file.seek(0)
    task_file.truncate()
    json.dump(tasks, task_file)
    task_file.close()
else:
    pass

# Debug
# print("NEW TASK FILE:")
# for k in tasks.keys():
#     print(k + ": ")
#     print(tasks[k])
# print('\n')

# Current problem: Deserialize the file, read contents, then write by TRUNCATION so as not to 
# repeatedly append the same thing (if modifying an existing task.)

"""
Further reading:
    1. File closing: https://realpython.com/why-close-file-python/
    2. Context managing: https://realpython.com/python-with-statement/
    3. 
"""