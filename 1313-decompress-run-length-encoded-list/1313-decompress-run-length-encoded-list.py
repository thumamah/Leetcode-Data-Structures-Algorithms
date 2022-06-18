class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
    # Approach 1
    # O(nm) time | O(n) space
        output = []
        # Looping through the nums for n-1 times with step size of 2.
        for i in range(0,len(nums)-1,2):
            #Frequency element is nums[i] whereas value is nums[i+1], 
            freq = nums[i]
            value = nums[i+1]
            # again loop through frequency and append the value to the output.
            for j in range(freq):
                output.append(value)      
        return output
        
    # Approach 2
    # O(n) time | O(n) space
#         decompressed = []
#         for i in range(0, len(nums)-1, 2):
        # decompress, then append the number that expanded based on frequency to the list in that order.
        # Don’t use append, it would actually just multiply the number. By doing what I did here,
        # you would multiply the number as a list object by the frequency.
#             decompressed += nums[i] * [nums[i+1]]
#         return decompressed
        
    
    
    
        # some other technique's for the above problem but not all test cases pass.
#         result = []
#         maps = {}
#         for i in range(0, len(nums), 2): 
#             if nums[i] not in maps and i != len(nums)-1:
#                 maps[nums[i]] = nums[i+1]
#                 print(maps)
#             elif isinstance(maps[nums[i]], list):
#                 maps[key].append(nums[i+1])
#             else:
#                 maps[nums[i]] = [maps[nums[i]], nums[i+1]]
                
#         for letter, count in maps.items():
            
#             if not isinstance(count, list):
                
#                 for value in count:
#                     n = value * count
#             else:
                
#                 n = letter * count//count
#                 print("e",n)
            
#             for i in range(0,n):
#                 result.append(count)
#                 print(n)
            
                
#         return result
        
        