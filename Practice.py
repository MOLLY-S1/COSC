def run_length_encode(nums):
    i = 0
    longest = []
    while i < len(nums):
        squence = 1
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            squence += 1
            i += 1

        cn = (nums[i], squence)
        longest.append(cn)
        i += 1

    return longest


print(run_length_encode([30, 20, 7, 7, 7, 7, 7]))
