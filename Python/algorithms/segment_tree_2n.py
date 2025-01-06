from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.n, self.T = len(nums), [0]*len(nums)*2
        for i in range(self.n):
            self.T[self.n+i] = nums[i]
        for i in range(self.n-1,-1,-1):
            self.T[i] = self.T[2*i] + self.T[2*i+1]
        print(self.T)

    def update(self, index: int, val: int) -> None:
        index += self.n
        self.T[index] = val
        while index > 1:
            index//=2
            self.T[index] = self.T[2*index] + self.T[2*index+1]

    def sumRange(self, left: int, right: int) -> int:
        L, R, result = left+self.n, right+self.n, 0
        while L<R:
            if L % 2 == 1:
                result += self.T[L]
                L += 1
            if R % 2 == 1:
                R -= 1
                result += self.T[R]
            L //= 2
            R //= 2
        return result

# Your NumArray object will be instantiated and called as such:
nums = [1,3,5]
obj = NumArray(nums)
#obj.update(index=0, val=2)
param_2 = obj.sumRange(left=0, right=2)
print(param_2)