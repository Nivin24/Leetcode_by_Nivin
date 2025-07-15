class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = sum(nums)
        digitSum = 0
        for n in nums:
            if n >= 10:
                for s in str(n):
                    digitSum += int(s)
            else:
                digitSum += n
        return abs(elementSum - digitSum)