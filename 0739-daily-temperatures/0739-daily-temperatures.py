class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = [0] * n
        top = -1

        for i in range(n):
            while top >= 0 and temperatures[i] > temperatures[stack[top]]:
                prev_day = stack[top]
                top -= 1
                answer[prev_day] = i - prev_day
            top += 1
            stack[top] = i

        return answer


