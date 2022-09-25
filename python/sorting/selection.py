"""
The selection module provides a function for sorting an
array using selection sort.
"""


def sort(a):
    """Rearranges the array in ascending order, using the natural order.
       :param a: the array to be sorted
    """

    N = len(a)
    for i in range(N):
        _min = i
        for j in range(i + 1, N):
            if a[j] < a[i]:
                _min = j
            _exch(a, i, _min)


def _exch(a, i, j):
    """Exchanges the items at index i and j in array a"""

    a[i], a[j] = a[j], a[i]


def _show(a):
    """Prints the content of the array a"""

    for i in range(len(a)):
        print(a[i], end=" ")


def main():
    """Reads strings from stdin, sorts them, and prints the result to
    stdout."""
    a = [5, 4, 3, 2, 1]
    sort(a)
    _show(a)


if __name__ == "__main__":
    main()
