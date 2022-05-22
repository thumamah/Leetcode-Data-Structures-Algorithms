class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
    # Optimised approach
    # O(n) time | O(1) space  
    
        for i in range(1, len(nums)):
            
            nums[i] += nums[i-1]
        return nums
    
    # Brute force approach
    # O(n) time | O(n) space
    
#         new = []
#         for i in range(len(nums)):
#             new.append(sum(nums[0:i+1]))
#         return new
                