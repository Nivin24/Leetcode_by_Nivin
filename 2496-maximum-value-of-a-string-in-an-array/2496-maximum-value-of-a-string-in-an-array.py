class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        max_val = 0
        for s in strs:
            if s.isdigit():
                val = int(s)
                if max_val < val:
                    max_val = val
            else:
                val = len(s)
                if max_val < val:
                    max_val = val
        return max_val
                    
                     