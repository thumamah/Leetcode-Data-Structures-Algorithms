class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        hashMap = {}
        goodPairs = 0
        
        for i in nums:
            if i in hashMap:
                goodPairs += hashMap[i]
                hashMap[i] += 1 
            else:
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
        