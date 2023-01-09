"""
These HTTP Errors are defined by Qualtrics. Documentation can be found
(https://api.qualtrics.com/instructions/docs/Instructions/responses.md)

"""


class Qualtrics400Error(Exception):
    """This Exception handles errors associated with the HTTP 400 (Bad Request) responses."""

    def __init__(self, msg):
        super().__init__(msg)
        self.status_code = 400


class Qualtrics401Error(Exception):
    """This Exception handles errors associated with the HTTP 401 (Unauthorized) responses."""

    def __init__(self, msg):
        super().__init__(msg)
        self.status_code = 401


class Qualtrics403Error(Exception):
    """This Exception handles errors associated with the HTTP 403 (Forbidden) responses."""

    def __init__(self, msg):
        super().__init__(msg)
        self.status_code = 403


class Qualtrics404Error(Exception):
    """This Exception handles errors associated with the HTTP 404 (Not Found) responses."""

    def __init__(self, msg):
        super().__init__(msg)
        self.status_code = 404


class Qualtrics429Error(Exception):
    """This Exception handles errors associated with the HTTP 429 (Too Many Requests) responses."""

    def __init__(self, msg):
        super().__init__(msg)
        self.status_code = 429


class Qualtrics500Error(Exception):
    """This Exception handles errors associated with the HTTP 500 (Internal Server Error) responses."""

    def __init__(self, msg):
        super().__init__(msg)
        self.status_code = 500


class Qualtrics503Error(Exception):
    """This Exception handles errors associated with the HTTP 503 (Temporary Internal Server Error) responses."""

    def __init__(self, msg):
        super().__init__(msg)
        self.status_code = 503


class Qualtrics504Error(Exception):
    """This Exception handles errors associated with the HTTP 504 (Gateway Timeout) responses."""

    def __init__(self, msg):
        super().__init__(msg)
        self.status_code = 504
