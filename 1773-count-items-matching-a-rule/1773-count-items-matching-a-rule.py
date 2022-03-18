class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        a=0;
        for i in range(len(items)):
            if ruleKey == "type":
                if ruleValue == items[i][0]:
                    a=a+1    
            if ruleKey == "color":
                if ruleValue == items[i][1]:
                    a=a+1    
            elif ruleKey == "name" :
                if ruleValue == items[i][2]:
                    a=a+1     
        return a
                