class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
       
        res = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for r in range(m):
            for c in range(n):
                res[c][r] = matrix[r][c]

        return res
