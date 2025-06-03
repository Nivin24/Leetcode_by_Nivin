class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_counts = [0] * 101  # Index 0 represents year 1950, up to 2050

        for birth, death in logs:
            year_counts[birth - 1950] += 1
            year_counts[death - 1950] -= 1

        max_population = year_counts[0]
        max_year = 1950
        for i in range(1, 101):
            year_counts[i] += year_counts[i - 1]
            if year_counts[i] > max_population:
                max_population = year_counts[i]
                max_year = 1950 + i

        return max_year



            
                