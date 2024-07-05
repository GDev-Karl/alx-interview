#!/usr/bin/python3
"""
Define is_winner function, a solution to the Prime Game problem
"""

def generate_primes(n):
    """Return list of prime numbers between 2 and n inclusive
       Args:
        n (int): upper boundary of range
    """
    primes_list = []
    sieve = [True] * (n + 1)
    for prime in range(2, n + 1):
        if sieve[prime]:
            primes_list.append(prime)
            for i in range(prime * 2, n + 1, prime):
                sieve[i] = False
    return primes_list


def is_winner(rounds, upper_limit):
    """
    Determines winner of Prime Game
    Args:
        rounds (int): no. of rounds of game
        upper_limit (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if rounds is None or upper_limit is None or rounds == 0 or upper_limit == 0:
        return None
    maria_score = 0
    ben_score = 0
    for _ in range(rounds):
        primes = generate_primes(upper_limit)
        if len(primes) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    return None

