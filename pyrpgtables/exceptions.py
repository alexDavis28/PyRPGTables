class PyRPGTablesException(Exception):
    pass

class ReaderError(PyRPGTablesException):
    pass

class InvalidFile(ReaderError):
    pass