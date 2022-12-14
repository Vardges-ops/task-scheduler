from typing import Optional

from Task_module.models.person_form import Person


class UserInterface:

    @staticmethod
    def create_user(
            usr_id: int, usr_name: str,
            usr_surname: str, usr_informer: str = 'telegram',
            usr_status: str = 'WAIT', task_id: Optional[int] = None
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
            return usr_obj

    @staticmethod
    def update_user(obj: Person, /, *, kwargs) -> Person:
        if kwargs:
            for k, v in kwargs.items():
                if hasattr(obj, k):
                    obj.k = v
                else:
                    print(f"Invalid argument name {k}")
        return obj

    @staticmethod
    def delete_user(obj: Person):
        pass

    @staticmethod
    def get_user(self):
        pass
