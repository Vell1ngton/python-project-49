def is_prime(n):
    if n <= 1:
        return 'no'
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 'no'
    return 'yes'