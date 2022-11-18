from Task_module.Interface.Exceptions.user_exceptions import UnrecognizedInformerException
from Task_module.Interface.task_interface import TaskInterface
from Task_module.Interface.user_interface import UserInterface
from Task_module.constants.user_constants import user_available_informers
from Task_module.models.helpers import generate_user_id


class BaseUser:
    def __init__(self, usr_name, usr_surname):
        usr_id = generate_user_id(1000)
        self.user_obj = UserInterface.create_user(
            usr_id=usr_id,
            usr_name=usr_name,
            usr_surname=usr_surname,
        )

    def set_informer(self, informer: str):
        if informer in user_available_informers:
            self.user_obj.informer = informer
            # TODO set connection
        else:
            raise UnrecognizedInformerException(
                f"Can't set informer. Please chose another one" # TODO this should also suggest available informers
            )

    def inform_user(self, message: str):
        pass


class TaskIteractions:
    pass


class UserTaskInterface:
    pass
