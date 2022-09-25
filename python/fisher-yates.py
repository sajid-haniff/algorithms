from random import randint


def shuffle(arr):
    n = len(arr)

    for i in range(n-1, 0, -1):
        # pick a random int from 0 to i
        j = randint(0, i+1)
        arr[i], arr[j] = arr[j], arr[i]
