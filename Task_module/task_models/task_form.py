from dataclasses import dataclass
from datetime import datetime
from typing import List


class Task(dataclass):
    _id: int
    urgent_lvl: str
    status: str
    create_time: datetime
    dest_time: datetime
    historical_times: List[datetime] = []
