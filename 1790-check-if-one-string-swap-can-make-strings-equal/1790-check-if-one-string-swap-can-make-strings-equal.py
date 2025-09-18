class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        n = len(s1)
        for i in range(n):
            for j in range(i+1,n):
                list_s1 = list(s1)
                list_s1[i], list_s1[j] = list_s1[j], list_s1[i]
                print("".join(list_s1), s2)
                if "".join(list_s1) == s2:
                    return True
        return False