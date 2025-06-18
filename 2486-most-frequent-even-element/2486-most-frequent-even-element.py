class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            if n % 2 == 0:
                if n not in freq:
                    freq[n] = 1
                else:
                    freq[n] += 1

        if len(freq) == 0:
            return -1

        most_freq = 0
        most_freq_value = float('inf')  

        for num, fr in freq.items():
            if fr > most_freq:
                most_freq = fr
                most_freq_value = num
            elif fr == most_freq:
                if num < most_freq_value:  # Tie in frequency → pick the smaller value
                    most_freq_value = num

        return most_freq_value