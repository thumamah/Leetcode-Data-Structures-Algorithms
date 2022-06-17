class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        decompressed = []
        
        for i in range(0, len(nums)-1, 2):
            decompressed += nums[i] * [nums[i+1]]
            print(nums[i] * [nums[i+1]])
            print(decompressed)
    
        return decompressed
        
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
        
        