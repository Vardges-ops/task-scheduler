from datetime import timedelta

from Task_module.models.task_form import Task


class TimerTask(Task): # TODO develop this one as well
    timer_delay: timedelta
