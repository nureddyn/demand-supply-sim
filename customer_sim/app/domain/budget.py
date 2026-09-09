

class Budget:
    def __init__(self, amount):
        if amount <= 0:
            raise ValueError("initial budget cannot be negative or 0")
        self.amount = budget


    def get_amount(self):
        ...

    def set_amount(self, amount):
        ...
