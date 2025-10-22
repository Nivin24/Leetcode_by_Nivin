class Solution:
    def generateTheString(self, n: int) -> str:
        s = ''
        if n % 2 == 1:
            for i in range(n):
                s += 'a'
            return s
        else:
            for i in range(n - 1):
                s += 'a'
            return s + 'b'