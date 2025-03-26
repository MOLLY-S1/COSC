# you will need to import math for your trophic_level_index function to work
import math


# trophic_level_index definition goes here
def trophic_level_index(chla, tn, tp):
    """ Takes values for CHLA, TN and TP and returns
        the average of the log transformed values.
    """
    tlc = 2.22 + 2.54 * math.log(chla, 10)
    tln = -3.61 + 3.01 * math.log(tn, 10)
    tlp = 0.218 + 2.92 * math.log(tp, 10)

    av = (tlc + tln + tlp) / 3
    tli3 = av
    return tli3


# years_to_achieve_goal_tli3 definition goes here
def years_to_achieve_goal_tli3(c_0, tn_0, tp_0, goal_tli3, yearly_reduction):
    """Find years to reach values of TLI3"""
    tli3 = trophic_level_index(c_0, tn_0, tp_0)
    year = 0
    while tli3 > goal_tli3:
        c_0 = c_0 * (1-(yearly_reduction / 100))
        tn_0 = tn_0 * (1-(yearly_reduction / 100))
        tp_0 = tp_0 * (1-(yearly_reduction / 100))
        year += 1
        tli3 = trophic_level_index(c_0, tn_0, tp_0)
    return year


# MAIN ROUTINE
years = years_to_achieve_goal_tli3(22, 200, 31, 5, 10)
print(years)
years = years_to_achieve_goal_tli3(80, 2300, 182, 5, 10)
print(years)
years = years_to_achieve_goal_tli3(22, 649, 51, 5, 10)
print(years)
