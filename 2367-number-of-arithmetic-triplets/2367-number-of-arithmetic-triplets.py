class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        u = 0
        num = len(nums)
        for i in range(num):
            for j in range(i+1,num):
                for k in range(j+1,num):
                    if i < j and j < k and nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        u += 1
        return u
        
        