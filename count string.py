def count_words(string):
    # Split the string by whitespace and count the resulting list
    words = string.split()
    return len(words)

# Example usage
input_string = input("Enter a string: ")
word_count = count_words(input_string)
print(f"Number of words: {word_count}")
