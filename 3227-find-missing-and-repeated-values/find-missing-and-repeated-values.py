class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_elements = n * n
        counts = [0] * (total_elements + 1)
        
        # Count frequencies of each number
        for row in grid:
            for val in row:
                counts[val] += 1
                
        repeated = -1
        missing = -1
        
        # Identify the repeated and missing numbers
        for i in range(1, total_elements + 1):
            if counts[i] == 2:
                repeated = i
            elif counts[i] == 0:
                missing = i
                
        return [repeated, missing]