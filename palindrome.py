string = input("Enter a string: ")

# Remove spaces and m it lowercase for a case-insensitive check
reverse_string = string.replace(" ", "").lower()

# Check if the processed string is the same forwards and backwards
is_palindrome = reverse_string == reverse_string[::-1]

print("Is palindrome:", is_palindrome)
