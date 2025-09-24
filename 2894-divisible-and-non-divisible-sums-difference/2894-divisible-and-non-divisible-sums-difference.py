class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1 = sum([x for x in range(1, n+1) if x % m != 0])
        nums2 = sum([x for x in range(1, n + 1) if x % m == 0])

        return nums1 - nums2