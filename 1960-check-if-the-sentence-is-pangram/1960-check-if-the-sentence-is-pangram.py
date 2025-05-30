class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for char in 'qwertyuioplkjhgfdsazxcvbnm':
            if char not in sentence:
                return False
        return True