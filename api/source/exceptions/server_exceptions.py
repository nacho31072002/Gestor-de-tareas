from fastapi import status

from .base_hhtp_exception import BaseHTTPException


class InternalServerError(BaseHTTPException):
    description = 'Unhandled error'
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    exception_code = 'API_UNALBLED_ERROR'


class NotImplemented(BaseHTTPException):
    description = 'Service not implemented yet'
    status_code = status.HTTP_501_NOT_IMPLEMENTED
    exception_code = 'API_ENDPOINT_NOT_IMPLEMENTED'


class BadRequestError(BaseHTTPException):
    description = 'Bad request'
    status_code = status.HTTP_400_BAD_REQUEST
    exception_code = 'API_BAD_REQUEST'