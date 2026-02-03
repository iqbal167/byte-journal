def find_task_by_id(tasks: list[dict], id: str) -> dict | None:
    for task in tasks:
        if task["id"] == id:
            return task
    return None