"""
This module contains a function that determines the winner of a game based on the given number
of iterations and a list of numbers.
"""


def isWinner(x, nums):
    """
    Determines the winner of a game based on the given number of iterations and a list of numbers.

    Args:
        x (int): The number of iterations.
        nums (List[int]): The list of numbers.

    Returns:
        str or None: The name of the winner ("Maria" or "Ben") if the game ends, or None if the game does not end.
    """
    if not x or not nums:
        return None
    if x < 1 or x > 100 or len(nums) < 1 or len(nums) > 100:
        return None

    winner = ""
    for _ in range(x):
        if isPrime(nums[0]):
            winner = "Maria"
            break
        elif isPrime(nums[1]):
            winner = "Ben"
            break

    if winner == "Maria":
        for i in range(x):
            if isPrime(nums[0]):
                nums.pop(0)
                nums = removeMultiples(nums, nums[0])
                if len(nums) == 0:
                    return "Maria"
            else:
                return "Ben"
    elif winner == "Ben":
        for i in range(x):
            if isPrime(nums[1]):
                nums.pop(1)
                nums = removeMultiples(nums, nums[1])
                if len(nums) == 0:
                    return "Ben"
            else:
                return "Maria"

    return None


def isPrime(num):
    """
    A function to check if a number is a prime number.

    Args:
        num (int): The number to be checked for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def removeMultiples(nums, num):
    """
    A function that removes multiples of a given number from a list of numbers.

    Args:
        nums (List[int]): The list of numbers to filter.
        num (int): The number whose multiples should be removed.

    Returns:
        List[int]: A new list containing only the numbers that are not multiples of the given number.
    """
    return [n for n in nums if n % num != 0]

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
