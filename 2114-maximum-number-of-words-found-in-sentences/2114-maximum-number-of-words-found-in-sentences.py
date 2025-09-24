class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        hashmap = {}
        for x in sentences:
            hashmap[x] = len(x.split(" "))

        return max(hashmap.values())

        