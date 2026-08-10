from http import HTTPStatus

class BaseException(Exception):
    def __init__(self, message: str, status: HTTPStatus):
        self.message = message
        self.status = status
        super().__init__(self.message)