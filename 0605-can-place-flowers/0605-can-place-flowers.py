class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(0, len(flowerbed)):
            if i>0 and flowerbed[i-1] == 1:
                continue
                
            if i == len(flowerbed) -1 and flowerbed[i] == 0:
                n-=1
                break
                
            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        
        
        return n <= 0
        