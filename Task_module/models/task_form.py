from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from Task_module.models.helpers import validate_model_attributes


@dataclass
class Task:
    id_: int
    urgent_lvl: str
    status: str
    create_time: datetime
    destination_time: datetime
    historical_times: List[datetime] = field(default_factory=list)

    def __post_init__(self):
        validate_model_attributes(self)
        print("A new person has been created")
