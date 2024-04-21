class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxy=max(candies)
        output=[]
        for i in candies:
            if i+extraCandies>=maxy:
                output.append(True)
            else:
                output.append(False)
        return output
         
        