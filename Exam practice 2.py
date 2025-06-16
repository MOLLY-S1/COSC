"""Question 25"""


def get_in():
    """f"""
    num = int(input("Enter an integer: "))
    num_l = list(str(num))
    return num_l


def timesing(nums):
    """f"""
    product = int(nums[0]) * int(nums[1])
    p_list = list(str(product))
    return p_list

def main():
    """f"""
    total = []
    nums = get_in()
    total.append("".join(nums))

    if len(nums) == 1:
        print("".join(total))

    else:

        new = timesing(nums)
        total.append("".join(new))

        while len(new) > 1:
            new = timesing(new)
            total.append("".join(new))

        print(" => ".join(total))


main()
