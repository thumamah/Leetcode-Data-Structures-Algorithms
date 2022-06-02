class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    
    # Approach 1
    # O(n) time | O(n) space
        result = []
        small = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] != nums[j] and nums[j] < nums[i]:
                    small += 1
            result.append(small)
            small = 0
        return result
        