# Create a python function to check whether a number is Prime or not

def is_prime(num):
    if num == 2 or num == 3:
        return f'{num} is a prime number'
    if num % 2 == 0 or num < 2:
        return f'{num} is not a prime number'
    for n in range(3, int(num**0.5)+1, 2):
        if num % n == 0:
            return f'{num} is not a prime number'
    return f'{num} is a prime number'


print(is_prime(3))  # 3 is a prime number
