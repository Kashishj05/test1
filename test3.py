# section d: Object-Oriented Programming & Advanced Concepts (30%)

from abc import ABC, abstractmethod

# Base class (abstract)

class BaseProcessor(ABC):
    @abstractmethod
    def process(self):
        pass

# LogFile class

class LogFile(BaseProcessor):
    def __init__(self, file_name):
        self.file_name = file_name
        self.records = []

    def load_file(self):
        try:
            with open(self.file_name, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        parts = line.split()
                        self.records.append({"level": parts[0], "message": " ".join(parts[1:])})
        except FileNotFoundError:
            print(f"File {self.file_name} not found!")

    def parse_records(self):
        return self.records

    def __str__(self):
        return f"LogFile({self.file_name}) with {len(self.records)} records"

    def __len__(self):
        return len(self.records)

    def process(self):
        self.load_file()

class UserAnalytics:
    def __init__(self, log_file_obj):
        self.logs = log_file_obj.records
        self.stats = {}

    def calculate_stats(self):
        self.stats = {"INFO":0,"ERROR":0,"WARNING":0}
        for r in self.logs:
            if r["level"] in self.stats:
                self.stats[r["level"]] += 1

    def generate_report(self):
        print(f"\nReport for {len(self.logs)} logs:")
        for k,v in self.stats.items():
            print(f"{k}: {v}")

def main():
    file_name = input("Enter log file name (e.g., log.txt): ")

    log_file = LogFile(file_name)
    log_file.process()
    print(log_file)           
    print("Total records:", len(log_file)) 
    ua = UserAnalytics(log_file)
    ua.calculate_stats()
    ua.generate_report()


if __name__ == "__main__":
    main                      
    