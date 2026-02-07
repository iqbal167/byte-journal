from model import Task, Status
from storage import load_state, save_state
from datetime import datetime, timezone
import helper

def add_task(args):
        description = args.description

        state = load_state()

        new_id = state["last_id"] + 1

        task = Task(id=new_id, description=description)

        state["tasks"].append(task.to_dict())
        state["last_id"] = new_id

        save_state(state)

        print(f"Task added successfully (ID: {new_id})")
   
def update_task(args):
    id = args.id
    description = args.description

    state = load_state()

    tasks = state["tasks"]

    found = helper.find_task_by_id(tasks, id)

    if not found:
        raise ValueError(f"Task with id {id} not found")

    found["description"] = description
    found["updated_at"] = datetime.now(timezone.utc).isoformat()

    save_state(state)

def delete_task(args):
    id = args.id

    state = load_state()

    tasks = state["tasks"]

    found = helper.find_task_by_id(tasks, id)
    if found:
        tasks.remove(found)
        save_state(state)

        return

    raise ValueError(f"Task with id {id} not found")

def mark_in_progress(args):
    id = args.id

    state = load_state()

    tasks = state["tasks"]

    found = helper.find_task_by_id(tasks, id)
    if not found:
        raise ValueError(f"Task with id {id} not found")

    found["status"] = Status.IN_PROGRESS.value
    found["updated_at"] = datetime.now(timezone.utc).isoformat()

    save_state(state)

def mark_done(args):
    id = args.id

    state = load_state()

    tasks = state["tasks"]

    found = helper.find_task_by_id(tasks, id)
    if not found:
        raise ValueError(f"Task with id {id} not found")

    found["status"] = Status.DONE.value
    found["updated_at"] = datetime.now(timezone.utc).isoformat()

    save_state(state)

def list_tasks(args):
    state = load_state()
    tasks = state["tasks"]

    if args.status:
        tasks = [task for task in tasks if task["status"] == args.status]

    print(tasks)
