def is_happy(num):
    """Check if a number is happy."""
    while num != 1 and num != 4:  # 4 indicates an unhappy loop
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

# List of numbers to check
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Find happy numbers in the list
happy_numbers = [n for n in numbers if is_happy(n)]
print("Happy numbers in the list:", happy_numbers)