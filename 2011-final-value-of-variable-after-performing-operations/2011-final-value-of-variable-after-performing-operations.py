class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        #maps = {"--X": -1, "X--": -1, "X++": 1, "++X": 1}
        return sum('+' in s or -1 for s in operations)
        
        
        
        
        
        
        # x = 0
        # for i in operations:
        #     if i == "--X":
        #         x -= 1
        #     elif i == "X--":
        #         x -= 1
        #     elif i == "++X":
        #         x += 1
        #     elif i == "X++":
        #         x += 1
        # return x
        