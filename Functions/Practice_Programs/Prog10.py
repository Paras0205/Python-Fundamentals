# top_n_frequent(nums, n)
# Input: list of numbers, and an integer n.
# Output: list of n most frequent numbers.

def top_n_frequent(nums, n):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    result = []

    for _ in range(n):
        max_key = None
        max_value = -1

        for key in freq:
            if freq[key] > max_value:
                max_value = freq[key]
                max_key = key

        result.append(max_key)
        del freq[max_key]

    return result


nums = [1, 1, 1, 2, 2, 3]
print(top_n_frequent(nums, 2))