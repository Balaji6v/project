string = "guvi geek s network private limited"
#count each other
vowels = {'a': 0, 'e' : 0, 'i' : 0, 'o': 0, 'u' : 0}

#intivative comparison the string lower case
string = string.lower()

#itereative over
for char in string:
    if char in vowels:
        vowels[char] +=1

#calculate number of vowel
total= sum(vowels.values())

print(f"total number of vowel:'{total}")
for vowels, count in vowels.items():
    print(f"count of '{vowels.upper():}' {count}")