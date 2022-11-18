import random


def validate_model_attributes(obj):
    for attr, attr_type in obj.__class__.__annotations__.items():
        if not isinstance(obj.__getattribute__(attr), attr_type):
            raise AttributeError(
                f"Parsed attribute {attr} is not type of {attr_type}"
            )


def generate_user_id(max_border: int) -> int:
    """
    This method is temporary
    :param max_border:
    :return:
    """
    number = random.randrange(1, max_border)
    return number
