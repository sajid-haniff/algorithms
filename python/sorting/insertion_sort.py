from typing import List, TypeVar

T = TypeVar("T")


def sort(a: List[T]):
    """sorts array a in ascending order, using the natural order
     :param a: the array to be sorted

    """

    # Sort a[] into increasing order
    N = len(a)
    for i in range(1, N):
        # Insert a[i] among a[i-1], a[i-2], a[i-3]...
        for j in range(i, 0, -1):
            if not _less(a[j], a[j - 1]):
                break
            _exch(a, j, j - 1)


def _less(v: T, w: T):
    return v < w


def _exch(a: List[T], i: int, j: int):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def show(a: List[T]):
    # Prints the array on a single line
    for item in a:
        print(item, end=" ")
    print()


def main():
    a = [5, 4, 3, 2, 1]
    sort(a)
    show(a)


if __name__ == "__main__":
    main()