class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in range(len(s)- 1):
            a = ord(s[i])
            b = ord(s[i + 1])
        
            result += abs(a - b)

        return result