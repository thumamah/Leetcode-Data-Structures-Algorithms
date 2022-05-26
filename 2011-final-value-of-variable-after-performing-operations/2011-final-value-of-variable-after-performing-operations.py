class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        #maps = {"--X": -1, "X--": -1, "X++": 1, "++X": 1}
        #sum(1 if '+' in op else -1 for op in operations)
        
        
        
        x = 0
        for i in operations:
            if "+" in i:
                x += 1
            else:
                x -= 1
        return x
        