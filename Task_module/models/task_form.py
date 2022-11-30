from dataclasses import dataclass, field
from datetime import datetime

from Task_module.models.helpers import validate_model_attributes


@dataclass
class Task:
    id_: int
    owner_id: int
    importance_lvl: str
    status: str
    create_time: datetime
    destination_time: datetime
    prev_time: datetime
    description: str = field(default_factory=str)

    def __post_init__(self):
        validate_model_attributes(self)
        print("A new person has been created")
