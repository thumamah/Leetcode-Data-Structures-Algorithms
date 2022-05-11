class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        #optimised approach
        #ans = list(range(2*(len(nums))))
        
        for i in range(len(nums)):
            nums.append(nums[i])
    
        return nums