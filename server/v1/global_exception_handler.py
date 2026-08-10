from fastapi import Request, FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
from v1.database import supabase_client
from v1.error.error_dao import ErrorDao
from v1.global_exceptions.base_exception import BaseException
import traceback

error_dao = ErrorDao(db_connection=supabase_client)

async def custom_base_exception_handler(request: Request, exc: BaseException):
    return JSONResponse(
        status_code=exc.status.value,
        content={
            "error": exc.message,
            "timestamp": datetime.now().isoformat()
        }
    )

async def global_exception_handler(request: Request, exc: Exception):
    await error_dao.log_error(
        error_class=exc.__class__.__name__,
        error_message=str(exc),
        stack_trace="".join(traceback.format_exception(type(exc), exc, exc.__traceback__)),
        effected_user_id=None
    )
    return JSONResponse(
        status_code=500,
        content={
            "error": "An unknown error blocked your request. Please try again later.",
            "timestamp": datetime.now().isoformat()
        },
    )

def add_exception_handlers(app: FastAPI):
    app.add_exception_handler(BaseException, custom_base_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)
