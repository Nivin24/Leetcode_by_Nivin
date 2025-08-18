from collections import Counter
class Solution:
    def checkRecord(self, s: str) -> bool:
        s_count = Counter(s)
        cons = 0
        if s_count['A'] < 2:
          for i in range(len(s)):
            if i+2 < len(s) and s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L':
              return False
          return True
        else:
          return False
              
