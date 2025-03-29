"""6 and above	Hypertrophic	Saturated
At least 5 and less than 6	Supertrophic	Very high
At least 4 and less than 5	Eutrophic	High
At least 3 and less than 4	Mesotrophic	Medium
At least 2 and less than 3	Oligotrophic	Low
At least 1 and less than 2	Microtrophic	Very low
Less than 1	Ultra-microtrophic	Practically pure
"""


# Define a function trophic_class(trophic_level_index) which returns the
# trophic classification (as a str) indicated by the Trophic Level Index
# value provided.


def trophic_class(trophic_level_index):
    """Classing trophic levels"""
    if 6 <= trophic_level_index:
        classification = "Hypertrophic"
        return classification
    elif 5 <= trophic_level_index < 6:
        classification = "Supertrophic"
        return classification
    elif 4 <= trophic_level_index < 5:
        classification = "Eutrophic"
        return classification
    elif 3 <= trophic_level_index < 4:
        classification = "Mesotrophic"
        return classification
    elif 2 <= trophic_level_index < 3:
        classification = "Oligotrophic"
        return classification
    elif 1 <= trophic_level_index < 2:
        classification = "Microtrophic"
        return classification
    elif trophic_level_index < 1:
        classification = "Ultra-microtrophic"
        return classification

# MAIN ROUTINE
classification = trophic_class(4.5)
print(classification)
classification = trophic_class(2)
print(classification)
classification = trophic_class(0.999)
print(classification)


