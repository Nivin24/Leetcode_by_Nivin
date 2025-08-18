class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        len_pref = len(pref)
        count = 0
        for w in words:
            if w[:len_pref] == pref:
                count += 1

        return count