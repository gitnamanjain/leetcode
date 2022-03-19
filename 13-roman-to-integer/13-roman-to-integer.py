class Solution:
    def romanToInt(self, s: str) -> int:
        val = [1000,500,100,50,10,5,1]
        rom = ["M","D","C","L","X","V","I"]
        result=0
        for i in range(len(s)):
            if(i<len(s)-1):
                if(val[rom.index(s[i])]>=val[rom.index(s[i+1])]):
                    result=result+val[rom.index(s[i])]
                else:
                    result=result-val[rom.index(s[i])]
            else:
                result=result+val[rom.index(s[i])]
        return result