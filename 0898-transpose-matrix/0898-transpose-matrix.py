class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        t_mat = []
        for i in range(n):
            t_mat.append([])
            for j in range(m):
                
                t_mat[i].append(matrix[j][i])
                    
        return t_mat