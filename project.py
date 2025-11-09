class Vehicle:
    def __init__(self, c): self.c = c
    def fare(self): return self.c * 100

class Bus(Vehicle):
    def fare(self): return super().fare() * 1.1

print("Total fare:", Bus(50).fare())
