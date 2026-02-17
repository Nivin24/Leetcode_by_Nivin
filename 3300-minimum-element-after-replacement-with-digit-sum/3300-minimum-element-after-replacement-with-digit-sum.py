class Solution:
    def minElement(self, nums: List[int]) -> int:
        a = []
        for n in nums:
            summ = 0
            sn = str(n)
            summ = sum([int(n) for n in sn])
            a.append(summ)
        return min(a)