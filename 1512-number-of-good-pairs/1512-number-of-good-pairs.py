class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
    # Optimized approach
    # O(n) time | O(1) space
    
        # define a map
        hashMap = {}
        goodPairs = 0
        
        #iterate over nums
        for i in nums:
            # check if number is in map
            if i in hashMap:
                # add the amount of times good pairs appears 
                goodPairs += hashMap[i]
                # increment the value of this key
                hashMap[i] += 1 
            else:
                # add this value to map
                hashMap[i] = 1
                
        return goodPairs
        
        
    # Brute Force approach
    # O(n^2) time | O(1) space
    
        # goodPairs = 0
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if nums[i] == nums[j] and i < j:
        #             goodPairs += 1
        # return goodPairs
        