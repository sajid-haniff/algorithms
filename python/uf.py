class UF:
    def __init__(self, n):
        self.count = n;               # number of components
        self.parent = list(range(n))  # parent[i] parent of i
        self.sz = [1] * n             # sz[i] = number of elements in subtree rooted at i

    def count(self):
        """Returns the umber of connected components"""
        return self.count

    def find(self, p):
        """Return the canonical element of the set containing p"""
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def connected(self, p, q):
        """Return True if p and q are in the same connected component"""
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """Merges component containing p with component containing q"""
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return

        # make smaller component point to larger component
        if self.sz[root_p] < self.sz[root_q]:
            self.parent[root_p] = root_q
            self.sz[root_q] += self.sz[root_p]
        else:
            self.parent[root_q] = root_p
            self.sz[root_p] += self.sz[root_q]

        self.count -= 1


if __name__ == '__main__':
    import sys

    n = int(sys.stdin.readline())
    uf = UF(n)
    for line in sys.stdin:
        p, q = [int(i) for i in line.split()]
        if uf.connected(p, q):
            continue
        else:
            uf.union(p, q)
            print("%s %s" % (p, q))
    print(uf.count, "components")

