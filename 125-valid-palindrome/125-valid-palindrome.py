class Solution:
    def isPalindrome(self, s: str) -> bool:
        plainstring = ""
        for i in s:
            if (i.isalnum()):
                plainstring = plainstring+i
        plainstring = plainstring.lower()
        if(len(plainstring)==0):
            return(True)
        for i,a in enumerate(plainstring):
            j=len(plainstring)-1
            while(i<=j):
                if(plainstring[i]==plainstring[j]):
                    i+=1
                    j-=1
                    continue
                else:
                    return(False)
            return(True)