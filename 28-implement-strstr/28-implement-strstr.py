class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(needle):
            checker = []
            # print(len(haystack))
            for i in range(len(haystack)):
                if((len(haystack)-(i))>=len(needle)):
                    if(needle[0]==haystack[i] and needle[len(needle)-1]==haystack[i+len(needle)-1]):
                        checker.append(i)
            k=0
            result=[1]*len(checker)
            for i in range(len(checker)):
                for j in range(checker[i],checker[i]+len(needle)):
                    if(k<len(needle)):
                        if(needle[k]!=haystack[j]):
                            result[i]=0
                            k=0
                            break
                        k+=1
            if 1 in result:
                return checker[result.index(1)]
            else:
                return -1
        else:
            return 0