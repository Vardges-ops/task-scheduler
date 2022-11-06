from datetime import timedelta

from Task_module.models.task_form import Task


class TimerTask(Task):
    timer_delay: timedelta
