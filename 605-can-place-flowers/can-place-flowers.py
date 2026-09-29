class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            # Check if current plot is empty and both neighbors (if they exist) are empty
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    flowerbed[i] = 1  # Plant a flower
                    n -= 1            # Decrement required flowers
                    
                    if n <= 0:
                        return True
                        
        return n <= 0