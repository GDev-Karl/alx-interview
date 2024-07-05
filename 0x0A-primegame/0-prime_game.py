def isWinner(x, nums):
    if not nums or x < 1:
        return None
    
    max_n = max(nums)
    
    # Sieve of Eratosthenes to find all prime numbers up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False

    # Precompute the number of prime picks possible for each n
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0
    
    # Simulate each game
    for n in nums:
        if prime_counts[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # Should output "Winner: Ben"
