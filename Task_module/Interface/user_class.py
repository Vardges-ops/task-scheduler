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
                _id=usr_id, name=usr_name, surname=usr_surname,
                informer=usr_informer, status=usr_status, ongoing_task_id=task_id
            )
        except AttributeError as atr_exc:
            print("Couldn't create user. Parsed wrong attribute type")
            print(atr_exc)
        else:
            return usr_obj

    @staticmethod
    def change_user(obj: Person) -> Person:
        pass

    @staticmethod
    def delete_user(obj: Person):
        pass
