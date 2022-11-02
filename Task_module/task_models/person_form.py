from dataclasses import dataclass, field
from typing import List


class Task:
    pass


@dataclass
class Person:

    _id: int
    name: str
    surname: str
    ongoing_task: Task # TODO refactor these to a separate interface
    status: str = 'WAIT'
    task_queue: List = field(default_factory=list)

    def __post_init(self):
        print("A new person has been created")
