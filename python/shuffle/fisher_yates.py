import random


def random_int(_min, _max):
    return random.randint(_min, _max)


def _exch(a, i, j):
    """Exchanges the items at index i and j in array a"""
    a[i], a[j] = a[j], a[i]


def shuffle_in_place(a):
    N = len(a)
    for curr_idx in range(N):
        random_idx = random_int(curr_idx, N - 1)
        _exch(a, random_idx, curr_idx)


def main():
    """Reads strings from stdin, shuffles them, and prints the resul"""

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffle_in_place(a)
    print(a)


if __name__ == "__main__":
    main()
