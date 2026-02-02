from model import Task
from storage import load_state, save_state
from datetime import datetime, timezone

def add_task(args):
        description = args.description
        task = Task(description=description)

        state = load_state()
        state["tasks"].append(task.to_dict())

        save_state(state)

        print(f"Adding task: {task.to_dict()}")
   
def update_task(args):
    id = args.id
    description = args.description

    state = load_state()

    tasks = state["tasks"]

    for task in tasks:
        if task["id"] == id:
            task["description"] = description
            task["updated_at"] = datetime.now(timezone.utc).isoformat()

            save_state(state)
            print(f"Updating task {id} with description: {description}")
            return 

    raise ValueError(f"Task with id {id} not found")

def delete_task(args):
    id = args.id
    print(f"Deleting task {id}")

def mark_in_progress(args):
    id = args.id
    print(f"Marking task {id} as in progress")

def mark_done(args):
    id = args.id
    print(f"Marking task {id} as done")

def list_tasks(args):
    status = args.status
    print(f"Listing tasks with status: {status}")
