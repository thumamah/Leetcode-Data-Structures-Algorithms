class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        output = []
        maxs = max(candies)
        l = len(candies)
        for i in range(l):
            if candies[i]+extraCandies >= max(candies):
                output.append(True)
            else:
                output.append(False)
        return output
    
    # l=len(candies)
    #     ans=[]
    #     for i in range(l):
    #         if candies[i]+extraCandies >= max(candies):
    #             ans.append(True)
    #         else:
    #             ans.append(False)
    #     return ans
        