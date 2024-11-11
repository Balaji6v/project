def longest_common_substring(str1, str2):
    longest_substr = ""
    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring = str1[i:j]
            if substring in str2 and len(substring) > len(longest_substr):
                longest_substr = substring
    return longest_substr

# Example usage
str1 = "abcde"
str2 = "abfce"
print("Longest common substring:", longest_common_substring(str1, str2))
