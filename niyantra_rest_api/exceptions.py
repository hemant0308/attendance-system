class UserNotFound(Exception):
    pass

class InvalidCredentials(Exception):
    pass

class NoResourceFound(Exception):
    pass

class ConstraintError(Exception):
    def __init__(self,message):
        super(ConstraintError,self).__init__(message)