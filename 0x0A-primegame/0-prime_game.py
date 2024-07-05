#!/usr/bin/python3
'''Prime Game'''


def isPrime(n):
    """
    A function to check if a given number is a prime number.
    Parameters:
        n (int): The number to check for primality.
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def isRoundWinner(n, x):
    """
    Determines the winner of a round in the Prime Game.

    Args:
        n (int): The number of integers in the round.
        x (int): The number of integers each player can remove in each turn.

    Returns:
        str: The name of the player who wins the round, or None if there is no winner.
    """
    list_ = [i for i in range(1, n+1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        currentPlayer = players[i % 2]
        for idx, num in enumerate(list_):
            if isPrime(num) and all(num % j != 0 for j in list_[:idx]):
                list_.pop(idx)
                break
        else:
            if currentPlayer == players[0]:
                return players[1]
            else:
                return players[0]
    return None


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game based on the number of rounds and the list of numbers.

    Args:
        x (int): The number of rounds to play.
        nums (List[int]): The list of numbers to play the game with.

    Returns:
        Optional[str]: The name of the winner if they won more than half the rounds, else None.
    """
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for n in nums[:x]:
        roundWinner = isRoundWinner(n, x)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    winner = max(winnerCounter, key=winnerCounter.get)
    return winner if winnerCounter[winner] > x // 2 else None
