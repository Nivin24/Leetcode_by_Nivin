class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if digits[k] % 2 == 1:
                        continue
                    if i == j or j == k or i == k:
                        continue
                    
                    val = digits[i] * 100 + digits[j] * 10 + digits[k]

                    res.add(val)
        return sorted(res)
