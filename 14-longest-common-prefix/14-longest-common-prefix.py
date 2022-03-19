class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstone=strs[0]
        if(len(strs)>1):
            strs.pop(0)
        result=[]
        for i in range(len(strs)):
            temp=""
            for x, y in zip(firstone, strs[i]):
                if x==y:
                    temp=temp+x
                else:
                    break
            result.append(temp)
        
        return min(result,default="")