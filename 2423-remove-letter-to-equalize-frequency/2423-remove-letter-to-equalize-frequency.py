class Solution:
    def equalFrequency(self, word: str) -> bool:
        from collections import Counter

        freq = Counter(word)

        for ch in list(freq.keys()):
            freq[ch] -= 1
            if freq[ch] == 0:
                del freq[ch]
            
            if len(set(freq.values())) == 1:
                return True

            freq[ch] = freq.get(ch, 0) + 1

        return False