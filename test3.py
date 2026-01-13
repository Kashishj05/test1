
from abc import ABC, abstractmethod
from collections import Counter
from typing import List, Dict, Iterator
import logging

logging.basicConfig(level=logging.INFO)

# ---------- Base Processor ----------

class BaseProcessor(ABC):
    @abstractmethod
    def process(self) -> None:
        """Execute the processing logic"""
        pass
# ---------- LogFile Class ----------

class LogFile(BaseProcessor):
    def __init__(self, file_name: str):
        self.file_name = file_name
        self._records: List[Dict[str, str]] = []

    def load_file(self) -> None:
        """Reads the log file line by line"""
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                for line in f:
                    record = self._parse_line(line)
                    if record:
                        self._records.append(record)
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_name}")
            raise
        except OSError as e:
            logging.error(f"I/O error: {e}")
            raise

    def _parse_line(self, line: str) -> Dict[str, str] | None:
        """Parses a single log line into a record"""
        line = line.strip()
        if not line:
            return None

        parts = line.split(maxsplit=1)
        if len(parts) < 2:
            logging.warning(f"Malformed log line skipped: {line}")
            return None

        return {
            "level": parts[0].upper(),
            "message": parts[1]
        }

    @property
    def records(self) -> List[Dict[str, str]]:
        """Read-only access to log records"""
        return list(self._records)

    def __iter__(self) -> Iterator[Dict[str, str]]:
        return iter(self._records)

    def __len__(self) -> int:
        return len(self._records)

    def __str__(self) -> str:
        return f"LogFile({self.file_name}) with {len(self)} records"

    def process(self) -> None:
        self.load_file()


# ---------- UserAnalytics Class ----------

class UserAnalytics:
    def __init__(self, log_file: LogFile):
        self.logs = list(log_file.records)   # copy for isolation
        self.stats: Counter[str] = Counter()

    def calculate_stats(self) -> None:
        self.stats = Counter(log["level"] for log in self.logs)

    def generate_report(self) -> None:
        print(f"\nReport for {len(self.logs)} logs:")
        for level, count in self.stats.items():
            print(f"{level}: {count}")


# ---------- Main ----------

def main() -> None:
    file_name = input("Enter log file name (e.g., log.txt): ").strip()

    if not file_name:
        print("Invalid file name")
        return

    try:
        log_file = LogFile(file_name)
        log_file.process()

        print(log_file)
        print("Total records:", len(log_file))

        analytics = UserAnalytics(log_file)
        analytics.calculate_stats()
        analytics.generate_report()

    except Exception:
        print("Failed to process log file. Check logs for details.")


if __name__ == "__main__":
    main()
