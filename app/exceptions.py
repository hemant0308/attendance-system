class CustomException(Exception):
    def __init__(self,message=None):
        super(Exception,self).__init__(message)

class ResourceNotFound(CustomException):
    def __init__(self, message='Resource Not Found'):
        super(ResourceNotFound,self).__init__(message)

class InvalidCredentials(CustomException):
    def __init__(self,message):
        super(ConstraintError,self).__init__(message)

class ConstraintError(CustomException):
    def __init__(self,message):
        super(ConstraintError,self).__init__(message)

class DuplicateEntry(CustomException):
    def __init__(self, message):
        super(DuplicateEntry, self).__init__(message)

class UnAuthorized(CustomException):
    def __init__(self,message):
        super(UnAuthorized, self).__init__(message)