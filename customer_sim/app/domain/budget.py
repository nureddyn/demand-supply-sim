import math
import sys

# budget generator will be responsible for a budget value bounded in the simulated market

# Value objects should be immutable
# budget_1 = Budget(5.0)
# budget_2 = Budget(10.0)
# budget_3 = Budget(budget_1.get_value() - budget_2.get_value())

class Budget:
    MAX_BUDGET = sys.float_info.max

    def __init__(self, value):
        if math.isnan(value):
            raise ValueError("Budget cannot be NaN")

        if value < 0:
            raise ValueError("Budget cannot be negative")

        if value >= self.MAX_BUDGET or math.isinf(value):
            raise ValueError("Budget cannot exceed maximum allowed float limit")

        self.value = value


    def get_value(self):
        ...

    def set_value(self, value):
        if math.isnan(value):
            raise ValueError("Budget cannot be NaN")

        if value < 0:
            raise ValueError("Budget cannot be negative")

        if value >= self.MAX_BUDGET or math.isinf(value):
            raise ValueError("Budget cannot exceed maximum allowed float limit")

        self.value = value
