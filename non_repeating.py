def find_non_repeating(lst):
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1
    for key, value in freq.items():
        if value == 1:
            return key
    return None  # If no non-repeating element is found

# Example
lst = [4, 5, 6, 7, 4, 5, 6]
print(find_non_repeating(lst))  # Output: 7
