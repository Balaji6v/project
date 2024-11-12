def is_anagram(str1, str2):
    # Anagrams must have the same length and the same sorted characters
    return sorted(str1) == sorted(str2)

# Example usage
string1 = "listen"
string2 = "silent"
print("Are the strings anagrams?", is_anagram(string1, string2))
