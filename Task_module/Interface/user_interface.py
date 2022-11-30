from typing import Optional

from Task_module.constants.user_constants import user_statuses
from Task_module.models.person_form import Person


class UserCRUD:  # TODO way for user identification from source, ex: telegram_id

    @staticmethod
    def create_user(
            usr_id: int, usr_name: str,
            usr_surname: str, usr_informer: str = 'telegram',
            usr_status: str = user_statuses[0], task_id: Optional[int] = None
    ) -> Optional[Person]:
        """under construction"""
        try:
            usr_obj = Person(
                id_=usr_id, name=usr_name, surname=usr_surname,
                informer=usr_informer, status=usr_status, ongoing_task_id=task_id
            )
        except AttributeError as atr_exc:
            print("Couldn't create user. Parsed wrong attribute type")
            print(atr_exc)
        else:
            return usr_obj # TODO fill data into DB

    @staticmethod
    def update_user(person_id: int, /, *, kwargs) -> Person:
        obj = UserCRUD.get_user(person_id)
        if kwargs:
            for k, v in kwargs.items():
                if hasattr(obj, k):
                    obj.k = v
                else:
                    print(f"Invalid argument name {k}")
        return obj

    @staticmethod
    def deactivate_user(person_id: int):
        user_obj = UserCRUD.get_user(person_id)
        user_obj.status = user_statuses[1]
        # TODO check if necessary do some actions, for example deactivate tasks as well
        pass

    @staticmethod
    def activate_user(person_id: int):
        user_obj = UserCRUD.get_user(person_id)
        user_obj.status = user_statuses[0]
        # TODO check if necessary do dome actions


    @staticmethod
    def get_user(person_id) -> Person:
        pass
