# Strategy pattern implementation
# utils/strategies.py
class Strategy:
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        return "Strategy A"