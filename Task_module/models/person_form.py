from dataclasses import dataclass, field
from typing import List, Optional

from Task_module.models.helpers import validate_model_attributes


@dataclass
class Person:

    id_: int
    name: str
    surname: str
    informer: str
    status: str
    ongoing_task_id: Optional[int] | None  # TODO refactor these to a separate interface
    task_queue: List = field(default_factory=list)

    def __post_init__(self):
        validate_model_attributes(self)
        print("A new person has been created")
