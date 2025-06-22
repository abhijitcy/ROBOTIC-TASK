def is_prime(n):#9
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(lst):
    return [x for x in lst if is_prime(x)]


original_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_list = filter_primes(original_list)
print(prime_list)
