from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        res = []

        for num in range(100, 1000, 2):  # only even numbers
            temp = Counter(map(int, str(num)))
            
            if all(count[d] >= temp[d] for d in temp):
                res.append(num)
        
        return res