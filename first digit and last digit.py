numbers = (int(input("enter the numbers:")))
numbers = -numbers
last_digit = numbers %10
while numbers >= 10:
    numbers //= 10
first_digit = numbers
sum_digits = first_digit + last_digit
print("sum of digits",sum_digits)

