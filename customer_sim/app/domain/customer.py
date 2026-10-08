class Customer:
    def __init__(self, budget):
        self.budget = budget
        self.wish_list = []

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, budget):
        self._budget = budget
