"""Question 30"""


class Whatsit:
    """f"""

    def __init__(self, name, weight, sound):
        """f"""
        self.name = name
        self.weight = weight
        self.sound = sound

    def __repr__(self):
        """f"""
        return f"{self.name} ({self.weight:.1f} kg) {" ".join(self.sound)}"

    def heavier_by(self, other):
        """f"""
        self.weight += other

    def teach(self, other):
        """f"""
        self.sound.append(other)

    def unteach(self, other):
        """f"""
        if other in self.sound:
            self.sound.remove(other)
        else:
            print(f"Error: {self.name} can't {other}")

thing = Whatsit("Rover", 10.4, ['Woof'])
print(thing)
thing.teach('Bark')
print(thing)
thing.heavier_by(1.002)
thing.teach('Woof')
print(thing)
thing.unteach('Woof')
print(thing)
thing.unteach('Woof')
print(thing)
thing.unteach('Miaow')
print(thing)
thing.unteach('Bark')
print(thing)