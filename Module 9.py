import numpy as np
def my_evens(my_numbers):
    """f"""
    return(my_numbers[my_numbers%2=0])

my_numbers = np.array([1, 2, 3, 4, 5])
even_numbers = my_evens(my_numbers)
print(even_numbers)