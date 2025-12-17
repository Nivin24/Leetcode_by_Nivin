class Solution:
    def checkDivisibility(self, n: int) -> bool:
        nn = str(n)
        sum_nn = 0
        prod_nn = 1
        for i in range(len(nn)):
            sum_nn += int(nn[i])

            prod_nn *= int(nn[i])

        total = sum_nn + prod_nn
        if n % total == 0:
            return True
        else:
            return False