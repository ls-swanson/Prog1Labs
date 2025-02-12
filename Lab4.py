def fibonacci(x):
    a = -1
    b = 1
    c = 1
    count = 0
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        while (count < x):
            c = a + b
            a = b
            b = c
            count += 1
        return c
def is_prime(n):
    a = 2
    isprime = True
    while a < n:
        if n % a == 0:
            isprime = False
        a += 1
    return isprime
def print_prime_factors(z):
    final_string = f'{z} ='
    if is_prime(z) == True:
        print(f'{z} = {z}')
    else:
        a = z
        b = 2
        while a > 1:
            while a % b == 0:
                a = a/b
                if final_string == f'{z} =':
                    final_string = final_string + f' {b}'
                else:
                    final_string = final_string + f' * {b}'
            b += 1
        print(final_string)
