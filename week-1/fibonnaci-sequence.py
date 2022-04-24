# Create a python function that when you input a number the function you have created checks whether the number belongs to the Fibonacci sequence or not

def checkfibonacci(n):
    # variables for generaating fibonacci sequenece
    a = 0
    b = 1
    # 0 and 1 are both fibonacci numbers
    if (n == a or n == b):
        return f'{n} belongs to the Fibonacci Sequence'

    # generating the fibonacci numbers until the generated number is less than  n
    c = a + b
    while(c <= n):
        if(c == n):
            return f'{n} belongs to the Fibonacci Sequence'
        a = b
        b = c
        c = a + b

    return f'{n} does not belong to the Fibonacci Sequence'


print(checkfibonacci(21))  # 21 belpngs to the Fibonacci Sequence
