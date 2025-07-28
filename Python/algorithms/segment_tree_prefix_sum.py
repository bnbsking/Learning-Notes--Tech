from typing import List


class PrefixSumSegmentTree:
    def __init__(self, A: List[int]):
        self.n = len(A)
        self.T = [0] * (4 * self.n)
        def build(node = 0, l = 0, r = self.n - 1):
            if l == r:
                self.T[node] = A[l]
            else:
                lnode, rnode, m = 2 * node + 1, 2 * node + 2, (l + r) // 2
                build(lnode, l, m), build(rnode, m + 1, r)
                self.T[node] = self.T[lnode] + self.T[rnode]
        build()

    def update(self, index: int, value: int):
        def renew(node = 0, l = 0, r = self.n - 1):
            if l == r:
                self.T[node] = value
            else:
                lnode, rnode, m = 2 * node + 1, 2 * node + 2, (l + r) // 2
                renew(lnode, l, m) if index <= m else renew(rnode, m + 1, r)
                self.T[node] = self.T[lnode] + self.T[rnode]
        renew()

    def search(self, x: int):
        def search(x, node = 0, l = 0, r = self.n - 1):
            if self.T[node] <= x:
                return -1
            elif l == r:
                return l
            else:
                lnode, rnode, m = 2 * node + 1, 2 * node + 2, (l + r) // 2
                return search(x, lnode, l, m) if x < self.T[lnode] else search(x - self.T[lnode], rnode, m + 1, r)
        return search(x)


A = [2, 3, 2, 4]
st = PrefixSumSegmentTree(A)

for i in range(4, 7):
    print(f"search {i} result:", st.search(i))  # 1, 2, 3

st.update(1, 4)  # A becomes [2, 4, 2, 4]

for i in range(4, 7):
    print(f"search {i} result:", st.search(i))  # 1, 1, 2
