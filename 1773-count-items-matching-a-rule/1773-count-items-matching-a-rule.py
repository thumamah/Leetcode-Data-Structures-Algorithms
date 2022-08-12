class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        
        res = 0
        typ = ['type', 'color', 'name']
        for i in range(len(items)):
            if ruleKey == typ[0] and ruleValue == items[i][0]:
                res+=1
            elif ruleKey == typ[1] and ruleValue == items[i][1]:
                res+=1
            elif ruleKey == typ[2] and ruleValue == items[i][2]:
                res+=1
        return res
        