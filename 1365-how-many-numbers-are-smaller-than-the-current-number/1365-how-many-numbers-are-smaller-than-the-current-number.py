class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
    # Approach 1
    # O(n^2) time | O(n) space
    
        # result = []
        # # store amount of smaller numbers than current
        # smallNumbers = 0
        # # iterate over nums
        # for i in range(len(nums)):
        #     # iterate over nums again to check for smaller numbers
        #     for j in range(len(nums)):
        #         # check if number is smaller than current
        #         if nums[i] != nums[j] and nums[j] < nums[i]:
        #             # count smaller number
        #             smallNumbers += 1
        #     # add it to result
        #     result.append(smallNumbers)
        #     # reset small number variable for next iteration.
        #     smallNumbers = 0
        # return result
    
    # Approach 2
    # O(n log(n)) time | O(n) space
        
#         map to store unique elements with their index
        maps = {}
        result = []
        # iterate over sorted list
        for i, j in enumerate(sorted(nums)):
#             if number not in map then add it assigning the index to it as well
            if j not in maps:
                maps[j] = i
#             iterate over the original list
        for n in nums:
#         for each number in nums, append to list according to the number we see in map.
            result.append(maps[n])
        return result
        