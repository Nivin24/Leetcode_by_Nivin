class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = []
        n1 = {}
        n2 = {}

        for i in range(len(nums1)):
            n1[nums1[i]] = n1.get(nums1[i], 0) + 1
        for j in range(len(nums2)):
            n2[nums2[j]] = n2.get(nums2[j], 0 ) + 1
        if len(nums1) < len(nums2):
            choose, other = n1, n2
        else:
            choose, other = n2, n1

        for key, count in choose.items():
            if key in other:
                for _ in range(min(count, other[key])):
                    inter.append(key)
        
        return inter

