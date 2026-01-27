def add_task(args):
    description = args.description
    print(f"Adding task: {description}")


def update_task(args):
    id = args.id
    description = args.description
    print(f"Updating task {id} with description: {description}")

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
