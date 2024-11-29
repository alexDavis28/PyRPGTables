class PyRPGTablesException(Exception):
    pass


class ReaderError(PyRPGTablesException):
    pass


class TableError(PyRPGTablesException):
    pass


class InvalidFile(ReaderError):
    pass


class InvalidTableJson(TableError):
    pass
