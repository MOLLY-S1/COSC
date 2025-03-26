"""Define a function trophic_level_index(chla , tn, tp) that takes values for Chorophyll-a (CHLA), Total Nitrogen (TN), and Total Phosphorus (TP) and returns the Trophic Index (TLI3) using the calculation below.

The TLI3 is calculated as the average of the three transformed values, where each value is transformed as follows:

tlc = 2.22 + 2.54 * log10CHLA

tln = -3.61 + 3.01 * log10TN

tlp = 0.218 + 2.92 * log10TP



For example, if CHLA=10, TN=100,  and TP=1000, then:

tlc = 2.22 + 2.54 * log1010 = 2.22 + 2.54 * 1 = 4.76

tln = -3.61 + 3.01 * log10100 = -3.61 + 3.01 * 2 = 2.410

tlp = 0.218 + 2.92 * log101000 = 0.218 + 2.92 * 3 = 8.978

The average of the three values is (4.76 + 2.410 + 8.978) / 3

given the following result

TLI3 = 5.383 (to 3 decimal places)

 Notes:

The notation log10x means the logarithm to base 10 of x, i.e. the power to which 10 must be raised to yield x.
In Python, log10x can be calculated (after importing the math module) as math.log(x, 10)
You can assume that CHLA, TN, and TP values are positive, i.e. greater than 0.
Your function should not round its result.
TN, TP, and CHLA are commonly used variable names in the literature, so you can use the following variable names in your code in this assignment: tn, tp, and chla, note that they are lower case."""

# Function
# Don't remove this import.

import math


# math.log(x, 10) will return log base 10 of x

def trophic_level_index(chla, tn, tp):
    """ Takes values for CHLA, TN and TP and returns
        the average of the log transformed values.
    """
    tlc = 2.22 + 2.54 * math.log(chla, 10)
    tln = -3.61 + 3.01 * math.log(tn, 10)
    tlp = 0.218 + 2.92 * math.log(tp, 10)

    av = (tlc + tln + tlp) / 3
    tli3 = f"{av:.3f}"
    return tli3


# Main Routine
# Lake Rotoehu
result = trophic_level_index(7.1, 302.75, 28.993)
print(f'{result}')
