
class BaseException(Exception):
    """Base class for all exceptions in this module."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.status_code = 500
        self.detail = "An error occurred"
        self.error_code = "UNKNOWN_ERROR"
        self.error_type = "UnknownError"
        self.error_message = message

class DatabaseConnectionError(BaseException):
    """Exception raised for errors in the database connection."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.status_code = 500
        self.detail = "Database connection error"
        self.error_code = "DB_CONN_ERR"
        self.error_type = "DatabaseError"
        self.error_message = message

class AppNotFoundException(BaseException):
    """Exception raised when the application is not found."""
    def __init__(self, app_name:str):
        super().__init__(f"Application '{app_name}' not found.")
        self.app_name = app_name
        self.status_code = 404
        self.detail = f"Application '{app_name}' not found."
        self.error_code = "APP_NOT_FOUND"
        self.error_type = "NotFoundError"
        self.error_message = f"Application '{app_name}' not found."
        