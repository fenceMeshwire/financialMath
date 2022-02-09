#!/usr/bin/env python3

# Python 3.9.5

# Capital_Value.py

class CapitalValue():
    def __init__(self, value, interest, years):
        self.value = value
        self.interest = interest
        self.years = years
        
    # Accumulation
    # Final value = current value * accumulation factor
    def accumulation(self):
        value_acc = self.value * (1 + self.interest) ** self.years
        return value_acc # accumulated value

    # Rediscount
    # Current value = final value * rediscount factor
    def rediscount(self):
        value_redisc = self.value * (1 + self.interest) ** - self.years
        return value_redisc # rediscounted value

oCapitalValue = CapitalValue(36000, 0.03, 25) # Value, interest, years
accVal = round(oCapitalValue.accumulation(), 2)
rediscVal = round(oCapitalValue.rediscount(), 2)

print('Accumulated value:', accVal)
print('Rediscounted value:', rediscVal)
