from .base_exception import BaseException
from http import HTTPStatus

class NotFoundException(BaseException):
    def __init__(self, message: str = "Resource not found."):
        super().__init__(message, HTTPStatus.NOT_FOUND)