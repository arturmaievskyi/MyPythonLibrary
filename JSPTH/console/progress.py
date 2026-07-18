

class Progress:
    def __init__(self, total):
        self.total = total
        self.current = 0

    def update(self, increment=1):
        self.current += increment
        self.display()

    def display(self):
        percent = (self.current / self.total) * 100
        print(f"Progress: {percent:.2f}% ({self.current}/{self.total})", end='\r')

    def complete(self):
        self.current = self.total
        self.display()
        print()  # Move to the next line after completion

    def reset(self):
        self.current = 0
        self.display()