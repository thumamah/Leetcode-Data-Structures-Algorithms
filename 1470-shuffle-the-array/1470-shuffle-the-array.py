class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
    
    # Brute Force approach
    # O(n) time | O(n) space
    
        result = []
        # iterate over nums n times
        for i in range(n):
            # add element from start(X elements)
            result.append(nums[i])
            # add element from the second half (Y elements)
            result.append(nums[i+n]) 
            
                 
        return result 