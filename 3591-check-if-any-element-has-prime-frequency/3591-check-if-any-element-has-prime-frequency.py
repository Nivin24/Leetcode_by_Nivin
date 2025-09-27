class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        from collections import Counter
        isprime = False
        freq = Counter(nums)
        
        for val in freq.values():
            isprime = True
            if val < 2:
                continue
            for i in range(2, int(val ** 0.5)+1):
                if val % i == 0:
                    isprime = False
            if isprime:
                return True

        return False