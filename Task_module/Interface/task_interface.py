from typing import Optional
from datetime import datetime
from Task_module.models.task_form import Task


class TaskInterface:
    @staticmethod
    def create_task(
            owner_id: int, task_id: int, urgent_lvl: str,
            status: str, repetitive: bool, destination_time: datetime
    ) -> Optional[Task]:
        """
        This method creates task object from given attributes validates and
        if it is valid returns it, else deletes it
        :param owner_id: task owners id
        :param task_id: new task object id
        :param urgent_lvl: new task object urgency level
        :param status: new task object status
        :param repetitive: new task object repetitiveness value
        :param destination_time: new task destination time
        :return: newly created task object
        """
        try:
            task_obj = Task(
                id_=task_id, owner_id=owner_id, importance_lvl=urgent_lvl, status=status,
                repetitive=repetitive, create_time=datetime.now(), destination_time=destination_time
            )
        except AttributeError as atr_exc:
            print("Couldn't create task. Parsed wrong attribute type")
            print(atr_exc)
            del task_obj
        else:
            return task_obj

    @staticmethod
    def update_task(obj_id: int, /, *, kwargs) -> Task:
        """
        This method finds task object with given id and changes its attribute
        with the given ones if they exist.
        This method should not change task objects destination_time attribute
        :param obj_id: task object id
        :param kwargs: attributes to be updated
        :return: new changed object
        """
        obj = TaskInterface.get_task(obj_id)
        if kwargs:
            for k, v in kwargs.items():
                if hasattr(obj, k):
                    obj.k = v
                else:
                    print(f"Invalid argument name {k}")
        return obj

    @staticmethod
    def set_task_new_time(obj_id: int, new_time: datetime):
        """
        This method finds task object with given id and replaces its destination time with the given new one.
        Old destination time is appended to object's history time list
        :param obj_id: task object id
        :param new_time: new destination time which will be set on time object
        :return: None
        """
        obj = TaskInterface.get_task(obj_id)
        old_time = obj.destination_time
        obj.destination_time = new_time
        obj.hist_time_list = old_time
        print(f"Changed task's destination time from {old_time} to {new_time}")

    @staticmethod
    def return_task_info(obj_id: int) -> str:
        """
        This method gets task by its id and shows information about it
        :param obj_id: objects id
        :return: None
        """
        obj = TaskInterface.get_task(obj_id)
        info = f"Task info: \nCreation time {obj.create_time}\nDestination time {obj.destination_time}\n" \
               f"Urgency level {obj.importance_lvl}\nStatus {obj.status}\nRepetitive {obj.repetitive}"
        return info

    @staticmethod
    def get_task(task_id: int) -> Task:
        pass

    @staticmethod
    def delete_task(task_id: int):
        pass
