class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1 = nums[:n]
        nums2 = nums[n:]
        result = []

        for i in range(n):
            result.append(nums1[i])
            result.append(nums2[i])

        return result