import math
import sys


class Budget:
    MAX_BUDGET = sys.float_info.max

    def __init__(self, value):
        self.check_invariants(value)
        self.value = value

    def check_invariants(self, value):
        if math.isnan(value):
            raise ValueError("Budget cannot be NaN")

        if value < 0:
            raise ValueError("Budget cannot be negative")

        if value > self.MAX_BUDGET or math.isinf(value):
            raise ValueError("""Budget cannot exceed maximum allowed float limit""")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self.check_invariants(value)
        self._value = value
