class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        l = arr[1] - arr[0]
        
        for i in range(1,len(arr)-1):
            l2 = arr[i+1] - arr[i]
            if l != l2:
                return False
            
        return True
            
            
            