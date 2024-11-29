import random
from dataclasses import dataclass
from . import exceptions

@dataclass
class TableResult:
    entry: str

@dataclass
class TableRow:
    row_text: TableResult
    roll_range: list[int]


class Table:
    def __init__(self, roll_values: set[int] = set(), rows: list[TableRow] = None) -> None:
        self.lookup_table: dict = {}
        self.roll_values = roll_values
        if rows:
            self.construct_table(rows)

    def roll(self) -> tuple[int, TableResult]:
        roll_result = random.choice(list(self.roll_values))
        return (roll_result, self.lookup_table[roll_result])

    def construct_table(self, rows: list[TableRow]) -> None:
        for row in rows:
            for value in row.roll_range:
                self.roll_values.add(value)
                self.lookup_table[value] = row.row_text

    def to_json(self) -> dict:
        return {
            "lookup_table": self.lookup_table,
            "roll_values": self.roll_values
        }

    def from_json(self, json_data: dict) -> None:
        try:
            self.roll_values = json_data["roll_values"]
            self.lookup_table = json_data["lookup_table"]
        except KeyError:
            raise exceptions.InvalidTableJson()
