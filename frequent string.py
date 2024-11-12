def most_frequent_char(s):
    max_count = 0
    most_frequent = ''

    for char in s:
        count = s.count(char)
        if count > max_count:
            max_count = count
            most_frequent = char

    return most_frequent


# Example usage
string = "hello world"
print("Most frequent character:", most_frequent_char(string))
