import argparse
import string
import service

parser = argparse.ArgumentParser(description= 'Task Tracker')
subparsers = parser.add_subparsers(dest='command', required=True)

# Add a new task
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("description", help= "Task description")
add_parser.set_defaults(func=service.add_task)

# Update a task
update_parser = subparsers.add_parser("update", help="Update a task")
update_parser.add_argument("id", type=str, help="Task ID")
update_parser.add_argument("description", type=str, help="Task Description")
update_parser.set_defaults(func=service.update_task)

# Delete a task
delete_parser = subparsers.add_parser("delete", help="Delete a task")
delete_parser.add_argument("id", type=str, help= "Task ID")
delete_parser.set_defaults(func=service.delete_task)

# Mark a task as in progress
mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark a task as in progress")
mark_in_progress_parser.add_argument("id", type=str, help= "Task ID")
mark_in_progress_parser.set_defaults(func=service.mark_in_progress)

# Mark a task as done
mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
mark_done_parser.add_argument("id", type=str, help="Task ID")
mark_done_parser.set_defaults(func=service.mark_done)

# List all tasks
list_parser = subparsers.add_parser("list", help="List all tasks")
list_parser.add_argument("status", nargs="?", default=None, help= "Task status (done/todo/in-progress)", choices=['done', 'in-progress', 'todo'])
list_parser.set_defaults(func=service.list_tasks)

# Parse the arguments
args = parser.parse_args()

# Call the function associated with the command
try:
    args.func(args)
except Exception as e:
    print(f"Error: {e}")
