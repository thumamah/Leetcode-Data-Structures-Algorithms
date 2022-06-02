class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        #return [candie + extraCandies >= max(candies) for candie in candies]
        
    # Approach 1
    # O(n) time | O(n) space
    
        output = []
        # iterate over candies
        for candy in range(len(candies)):
            # check if current candy + extra candy is >= than all other candies
            if candies[candy]+extraCandies >= max(candies):
                output.append(True)
            else:
                output.append(False)
        return output
    