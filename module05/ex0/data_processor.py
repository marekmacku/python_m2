from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._items: list[tuple[int, str]] = []
        self._next_rank: int = 0
        self.total: int = 0
        self.name: str = "DataProcessor"

    def __len__(self) -> int:
        return len(self._items)

    def _store(self, value: str) -> None:
        self._items.append((self._next_rank, value))
        self._next_rank += 1
        self.total += 1

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self._items:
            raise IndexError("No data to output")
        return self._items.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Numeric Processor"

    @staticmethod
    def _is_number(value: typing.Any) -> bool:
        return isinstance(value, (int, float)) and not isinstance(value, bool)

    def validate(self, data: typing.Any) -> bool:
        if self._is_number(data):
            return True
        if isinstance(data, list):
            return all(self._is_number(x) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._store(str(item))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Text Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._store(item)
        else:
            self._store(data)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Log Processor"

    @staticmethod
    def _is_log_dict(value: typing.Any) -> bool:
        if not isinstance(value, dict):
            return False
        if "log_level" not in value or "log_message" not in value:
            return False
        for key, val in value.items():
            if not isinstance(key, str) or not isinstance(val, str):
                return False
        return True

    def validate(self, data: typing.Any) -> bool:
        if self._is_log_dict(data):
            return True
        if isinstance(data, list):
            return all(self._is_log_dict(x) for x in data)
        return False

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]],
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        entries: list[dict[str, str]]
        if isinstance(data, dict):
            entries = [data]
        else:
            entries = data
        for entry in entries:
            self._store(f"{entry['log_level']}: {entry['log_message']}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    np: NumericProcessor = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
    print(
        "Test invalid ingestion of string 'foo' without prior validation:"
    )
    try:
        np.ingest("foo")
    except ValueError as e:
        print(f"Got exception: {e}")
    numeric_batch: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_batch}")
    np.ingest(numeric_batch)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = np.output()
        print(f"Numeric value {rank}: {value}")

    print("Testing Text Processor...")
    tp: TextProcessor = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    text_batch: list[str] = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_batch}")
    tp.ingest(text_batch)
    print("Extracting 1 value...")
    rank, value = tp.output()
    print(f"Text value {rank}: {value}")

    print("Testing Log Processor...")
    lp: LogProcessor = LogProcessor()
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    log_batch: list[dict[str, str]] = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_batch}")
    lp.ingest(log_batch)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = lp.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
