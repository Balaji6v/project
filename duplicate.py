def duplicates_in_three_lists(list1, list2, list3):
    # Use set intersections to find common elements
    duplicates = set(list1) & set(list2) & set(list3)
    return list(duplicates)

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

# Find duplicates
duplicates = duplicates_in_three_lists(list1, list2, list3)
print("Duplicates in all three lists:", duplicates)

