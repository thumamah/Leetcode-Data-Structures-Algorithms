class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        # Optimised approach
        # O(n) time | O(n) space
        
        n = len(nums)
        for i in range(n):
            nums[i] = (n * (nums[nums[i]] % n) + nums[i])
              
        for i in range(n):
            nums[i] = ((nums[i] // n))
        
        return nums
    
    
        # brute force
        # O(n) time | O(n) space
        
#       ans = []

#       for i in range(len(nums)):
#       ans.append(nums[nums[i]])

#       return ans

        