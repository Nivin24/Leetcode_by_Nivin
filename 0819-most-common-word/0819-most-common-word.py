import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'[a-z]+', paragraph.lower())
        banned_set = set(banned)

        freq = {}
        for w in words:
            if w not in banned_set:
                freq[w] = freq.get(w, 0) + 1

        return max(freq, key= freq.get)
        