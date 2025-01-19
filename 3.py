def is_prime(num):
    for i in range(2, int(num**0.5) + 2):
        if num % i == 0 and num != 2: return False
    return True

def prime_list(num1, num2):
    list_ = []
    for i in range(num1, num2 + 1):
        if is_prime(i): list_.append(i)
    return list_

print(prime_list(11, 20))
print(prime_list(1, 100))
