class UserExceptions(Exception):
    """User actions base exception"""


class UserArgumentException(UserExceptions):
    """Throw when user has not given all necessary creation arguments"""


class UnrecognizedInformerException(UserExceptions):
    """Throw this when unrecognized informer is sent to registered"""


class WrongSecretInput(UserExceptions):
    """Throw when the secret under check does not match with the real one"""
