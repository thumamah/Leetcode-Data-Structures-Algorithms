class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
    # Approach 1
    # O(n) time | O(n) space
    
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target
        