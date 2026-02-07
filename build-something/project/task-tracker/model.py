from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum

class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

@dataclass
class Task:
    description: str
    id: int
    status: Status = Status.TODO
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @staticmethod
    def from_dict(data: dict): 
        return Task(
            description=data["description"],
            id=data["id"],
            status=Status(data["status"]),
            created_at=data["created_at"],
            updated_at=data["updated_at"],
        )




