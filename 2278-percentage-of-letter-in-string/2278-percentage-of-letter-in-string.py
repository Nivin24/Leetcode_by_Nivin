class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for w in s:
            if letter == w:
                count += 1
        perc = count / len(s) * 100
        return floor(perc)
        