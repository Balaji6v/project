prime_numbers = [10,501,22,37,100,999,87,351]
prime_list = []
for num in (prime_numbers):
    if num <= 1:
        continue
    is_prime = True
    for i in range (2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(num)
        print("prime number",prime_list)



