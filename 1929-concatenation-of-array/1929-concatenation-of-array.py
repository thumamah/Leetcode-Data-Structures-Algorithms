class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # Optimised approach
        # O(n) time | O(n) space
 
        for i in range(len(nums)):
            nums.append(nums[i])
    
        return nums
    
    
        # brute force
        # O(n) time | O(n) space


        #      ans = list(range(2*(len(nums))))

        #         for i in range(len(nums)):
        #             ans[i] = nums[i]
        #             ans[i+len(nums)] = nums[i]

        #         return ans