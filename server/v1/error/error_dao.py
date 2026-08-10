class ErrorDao:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    async def log_error(self, error_class: str, error_message: str, stack_trace: str, effected_user_id: str = None):
        data = {
            "error_class": error_class,
            "error_message": error_message,
            "stack_trace": stack_trace,
            "effected_user": effected_user_id
        }
        self.db_connection.table("errors").insert(data).execute()