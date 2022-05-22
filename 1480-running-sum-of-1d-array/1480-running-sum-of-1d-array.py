class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new = []
        
        for i in range(len(nums)):
            new.append(sum(nums[0:i+1]))
        return new
                