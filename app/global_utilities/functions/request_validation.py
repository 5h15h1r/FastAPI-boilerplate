# from fastapi import FastAPI, Request, status
# from fastapi.responses import JSONResponse
# from typing import Callable


# async def validation_exception_handler(request: Request, exc: Exception):
#     """
#     Handler for validation exceptions
#     """
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content={"status": status.HTTP_422_UNPROCESSABLE_ENTITY, "message": str(exc)},
#     )


# async def general_exception_handler(request: Request, exc: Exception):
#     """
#     Handler for general exceptions
#     """
#     return JSONResponse(
#         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#         content={"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": str(exc)},
#     )


# def register_exception_handlers(app: FastAPI):
#     """
#     Register exception handlers to the FastAPI application
#     """
#     from fastapi.exceptions import RequestValidationError

#     app.add_exception_handler(RequestValidationError, validation_exception_handler)
#     app.add_exception_handler(Exception, general_exception_handler) 