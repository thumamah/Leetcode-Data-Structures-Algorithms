class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        # accounts = [[1,5],[7,3],[3,5]]
        
    # Brute Force approach
    # O(n) time | O(n) space
        
        maxList = 0
        
        for account in range(len(accounts)):
            wealth = sum(accounts[account])
            maxList = max(maxList, wealth)
            
        return maxList
        
    # Brute Force approach
    # O(n) time | O(n) space
        
#         maxList = []
        
#         for account in range(len(accounts)):
#             wealth = sum(accounts[account])
#             maxList.append(wealth)
            
#         return max(maxList)