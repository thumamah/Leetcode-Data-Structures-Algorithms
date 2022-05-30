class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
    # Approach 1
    # O(n) time | O(n) space
    
        output = []
        # iterate over candies
        for i in range(len(candies)):
            # check if current candy + extra candy is >= to all other candies
            if candies[i]+extraCandies >= max(candies):
                output.append(True)
            else:
                output.append(False)
        return output
        