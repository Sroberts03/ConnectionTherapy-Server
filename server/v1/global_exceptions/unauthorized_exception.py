from .base_exception import BaseException
from http import HTTPStatus

class UnauthorizedException(BaseException):
    def __init__(self, message: str = "You are not authorized to take this action."):
        super().__init__(message, HTTPStatus.UNAUTHORIZED)