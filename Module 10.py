class Fraction:
    """represents a fraction consisting of a numerator and a denominator"""

    def __init__(self, numerator, denominator):
        """f"""
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        """add"""
        top = (self.numerator * other.denominator + self.denominator * other.numerator)
        bottom = self.denominator * other.denominator
        if top > bottom:
            nums = bottom
        else:
            nums = top
        while (top % nums != 0) or (bottom % nums != 0):
            nums -= 1
        newx = top / nums
        newy = bottom / nums
        return f"({int(newx)}/{int(newy)})"

    def __sub__(self, other):
        """sub"""
        top = (self.numerator * other.denominator - self.denominator * other.numerator)
        bottom = self.denominator * other.denominator
        if top > bottom:
            nums = bottom
        else:
            nums = top
        while (abs(top) % nums != 0) or (abs(bottom) % nums != 0):
            nums -= 1
        newx = top / nums
        newy = bottom / nums
        return f"({int(newx)}/{int(newy)})"

    def __mul__(self, other):
        """multiply"""
        top = (self.numerator * other.numerator)
        bottom = (self.denominator * other.denominator)
        if top >= bottom:
            nums = bottom
        else:
            nums = top
        while (abs(top) % nums != 0) or (abs(bottom) % nums != 0):
            nums -= 1
        newx = top / nums
        newy = bottom / nums
        return f"({int(newx)}/{int(newy)})"

    def __truediv__(self, other):
        """divide"""
        if (self.denominator * other.numerator) == 0:
            raise ZeroDivisionError
        else:
            top = (self.numerator * other.denominator)
            bottom = (self.denominator * other.denominator)
            if top >= bottom:
                nums = bottom
            else:
                nums = top
            while (abs(top) % nums != 0) or (abs(bottom) % nums != 0):
                nums -= 1
                print("nums")
            newx = top / nums
            newy = bottom / nums
            return f"({int(newx)}/{int(newy)})"


    def __repr__(self):
        """f"""
        if self.numerator >= self.denominator:
            nums = self.denominator
        else:
            nums = self.numerator
        while (abs(self.numerator) % nums != 0) or (abs(self.denominator) % nums != 0):
            nums -= 1
        newx = self.numerator / nums
        newy = self.denominator / nums
        return f"({int(newx)}/{int(newy)})"

half = Fraction(1, 2)
two_thirds = Fraction(2, 3)
product = half * two_thirds
print(f"{half} * {two_thirds} = {product}")

x = Fraction(2, 3)
y = Fraction(4, 5)
diff = x - y
print(f"{x} - {y} = {diff}")