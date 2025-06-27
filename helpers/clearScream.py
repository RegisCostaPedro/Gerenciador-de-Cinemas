import os

class Helpers:
    def clearScreen():
     return os.system(
            'cls' if os.name == 'nt' else 'clear'
        )