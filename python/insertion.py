class Insertion:

    # Exchange a[i] and a[j]
    @classmethod
    def exchange(cls, a, i, j):
        a[i], a[j] = a[j], a[i]

    @classmethod
    def sort(cls, a):
        n = len(a)
        for i in range(1, n):
            j = i
            while (j > 0) and (a[j] < a[j - 1]):
                Insertion.exchange(a, j - 1, j)
                j -= 1


def main():
    import stdio

    a = stdio.readAllStrings()
    Insertion.sort(a)
    for s in a:
        stdio.write(s + ' ')
    stdio.writeln()


if __name__ == '__main__':
    main()




