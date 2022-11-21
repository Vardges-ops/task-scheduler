from Task_module.Interface.Exceptions.user_exceptions import UnrecognizedInformerException, WrongSecretInput, \
    UserArgumentException
from Task_module.Interface.task_interface import TaskCRUD
from Task_module.Interface.user_interface import UserCRUD
from Task_module.constants.user_constants import user_available_informers
from Task_module.models.helpers import generate_user_id


############
# TODO secret should be created in a convenient place so the system can access it and security may be set
# TODO secret should contain user id and tokenized so, if needed, user id may be detokenized from secret

class BaseUser:
    def __init__(self, usr_id=None, usr_name=None, usr_surname=None):
        if usr_id is None:
            if not all((usr_name, usr_surname)):
                raise UserArgumentException(
                    "Input user full name for registration"
                )
            usr_id = generate_user_id(1000)
            self.user_obj = UserCRUD.create_user(
                usr_id=usr_id,
                usr_name=usr_name,
                usr_surname=usr_surname,
            )
        else:
            self.user_obj = UserCRUD.get_user(usr_id)

    def set_informer(self, informer: str):
        if informer in user_available_informers:
            self.user_obj.informer = informer
            # TODO set connection
        else:
            raise UnrecognizedInformerException(
                f"Can't set informer. Please chose another one" # TODO this should also suggest to user, available informers
            )

    def inform_user(self, message: str):
        pass

    def activate_user(self, secret: str):
        id_ = None
        pass

    def deactivate_user(self, secret: str):
        origin_secret = ''  # TODO this initially should be created somewhere so we can have it anytime and then should be taken from DB and then checked
        if secret == origin_secret:
            UserCRUD.deactivate_user(self.user_obj.id_)
        else:
            raise WrongSecretInput(
                f"{secret} secret you have input doesn't match with the real one"
            )

class RegistrateUser:
    """This class should registrate(manipulate) user, like checking login, password,
     create secret and eventually return user object"""
    pass


class TaskIteractions:
    pass


class UserTaskInterface:
    pass
