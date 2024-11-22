def find_minimum(lst):
    if lst:  # Check if the list is not empty
        min_value = min(lst[0], lst[-1])  # Minimum is either the first or last element
        print(min_value)

# Example 1: Ascending Order
lst1 = [1, 2, 3, 4, 5]
find_minimum(lst1)  # Output: 1

# Example 2: Descending Order
lst2 = [5, 4, 3, 2, 1]
find_minimum(lst2)  # Output: 1
