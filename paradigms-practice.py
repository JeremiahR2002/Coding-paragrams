class Podracer:
    def __init__ (self, max_speed, condition, price )
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

def repair(self):
    self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
       return self.max_speed * 2


class SebulbasPod(Podracer):
    def flame_jet(self,other):
        return other.condition = "trashed"

# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

# We use inheritance in order to inherit the Podracer class to the other classes for the properties making it easier for us.
# I also believe encapsulation is also used by using classes, and defs in order to make the program easier to read aswell as easier to use

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?