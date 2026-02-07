def find_task_by_id(tasks: list[dict], id: int) -> dict | None:
    for task in tasks:
        if task["id"] == (id):
            return task
    return None