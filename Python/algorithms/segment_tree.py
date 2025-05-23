from typing import List


class SegmentTree:

    def __init__(self, nums: List[int]):
        self.n, self.T = len(nums), [0] * (len(nums) * 4)
        def build(node = 0, l = 0, r = self.n - 1):
            if l == r:
                self.T[node] = nums[l] 
            else:
                lnode, rnode, m = 2 * node + 1, 2 * node + 2, (l + r) // 2
                build(lnode, l, m), build(rnode, m + 1, r)
                self.T[node] = self.T[lnode] + self.T[rnode] 
        build()

    def update(self, index: int, val: int) -> None:
        def renew(node = 0, l = 0, r = self.n - 1):
            if l == r:
                self.T[node] = val
            else:
                lnode, rnode, m = 2 * node + 1, 2 * node + 2, (l + r) // 2
                renew(lnode, l, m) if index <= m else renew(rnode, m + 1, r)
                self.T[node] = self.T[lnode] + self.T[rnode] 
        renew()

    def sumRange(self, ql: int, qr: int) -> int:
        def query(node = 0, l = 0, r = self.n - 1):
            if qr < l or ql > r:
                return 0
            elif ql <= l and r <= qr:
                return self.T[node]
            else:
                lnode, rnode, m = 2 * node + 1, 2 * node + 2, (l + r) // 2
                return query(lnode, l, m) + query(rnode, m + 1, r)
        return query()
    

A = [1,2,3,4,5]
st = SegmentTree(A)
print(st.sumRange(0, 2))  # 6
print(st.sumRange(1, 3))  # 9
print(st.sumRange(0, 4))  # 15
st.update(1, 10)  # A becomes [1,10,3,4,5]
print(st.sumRange(0, 2))  # 14
print(st.sumRange(1, 3))  # 17
print(st.sumRange(0, 4))  # 23
