def validate_model_attributes(obj):
    for attr, attr_type in obj.__class__.__annotations__.items():
        if not isinstance(obj.__getattribute__(attr), attr_type):
            raise AttributeError(
                f"Parsed attribute {attr} is not type of {attr_type}"
            )
