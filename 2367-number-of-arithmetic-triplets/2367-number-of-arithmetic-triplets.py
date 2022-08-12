class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
    # Approach 1
    # O(n^3) time | O(1) space
        u = 0
        num = len(nums)
        for i in range(num):
            for j in range(i+1,num):
                for k in range(j+1,num):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        u += 1
        return u
    
    # Approach 2
    # O() time | O() space
    
        
        