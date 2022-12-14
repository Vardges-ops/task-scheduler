from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from Task_module.models.helpers import validate_model_attributes


@dataclass
class Task:
    id_: int
    owner_id: int
    importance_lvl: str
    status: str
    repetitive: bool
    create_time: datetime
    destination_time: datetime
    hist_time_list: List[datetime] = field(default_factory=list)

    def __post_init__(self):
        validate_model_attributes(self)
        print("A new person has been created")
