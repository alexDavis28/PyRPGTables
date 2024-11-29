import re
from abc import ABC
from . import tables
from . import exceptions


class Reader(ABC):
    def __init__(self) -> None:
        super().__init__()

    def read(self, file: str) -> tables.Table:
        pass

    @staticmethod
    def _extract_row(row: str) -> tables.TableRow:
        """Create a row obect from a string

        Args:
            row (str): The string of the row, in some form similar t:
            "1-2: Row Text"

        Returns:
            tables.TableRow: Parsed form of the row
        """
        # Detect range patterns of sort 1-2
        if search := re.search(r"^(\d+)-(\d+)", row):
            low, high = [int(i) for i in search.group().split("-")]
            roll_range = [i for i in range(low, high+1)]

        # Detect range patterns of sort 1:2
        elif search := re.search(r"^(\d+)(:(\d+))+", row):
            low, high = [int(i) for i in search.group().split(":")]
            roll_range = [i for i in range(low, high+1)]

        # Detect range patterns of sort 1 or 1,2
        elif search := re.search(r"^(\d+)(, *(\d+))*", row):
            roll_range = [int(i.strip()) for i in search.group().split(",")]

        row_text = row[search.end():]
        return tables.TableRow(row_text=row_text, roll_range=roll_range)


class TXTReader(Reader):
    def __init__(self) -> None:
        super().__init__()

    def read(self, file: str) -> tables.Table:
        if not file.endswith(".txt"):
            raise exceptions.InvalidFile("Path not a .txt file")

        with open(file, "r") as f:
            lines = f.readlines()

        rows = [self._extract_row(r) for r in lines]
        table = tables.Table(rows=rows)
        return table
