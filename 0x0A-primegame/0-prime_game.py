#!/usr/bin/python3
'''Prime Game'''

def isPrime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2)) + 1, 2):
            if n % i == 0:
                return False
        return True

def isRoundWinner(n, x):
    '''find round winner'''
    nums = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        currentPlayer = players[i % 2]
        selectedIdxs = []
        prime = -1
        for idx, num in enumerate(nums):
            if isPrime(num):
                prime = num
                selectedIdxs.append(idx)
        if prime == -1:
            return players[(i + 1) % 2]
        for idx in selectedIdxs:
            del nums[idx]
    return players[(n - 1) % 2]

def isWinner(x, nums):
    '''finds the winner'''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundWinner = isRoundWinner(nums[i], x)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None
