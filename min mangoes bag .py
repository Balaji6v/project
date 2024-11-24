def minimize_difference(bags, m):
    # Sort the bags to enable contiguous selection for minimal difference
    bags.sort()
    n = len(bags)

    # Initialize the minimum difference to a large value
    min_difference = float('inf')

    # Iterate over possible subsets of size m
    for i in range(n - m + 1):
        # Difference between max and min in this subset
        difference = bags[i + m - 1] - bags[i]
        # Update the minimum difference
        min_difference = min(min_difference, difference)

    return min_difference


# Input: Mangoes in each bag and number of students
bags = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7  # Number of students

# Output the result
result = minimize_difference(bags, m)
print(f"The minimum difference is: {result}")
