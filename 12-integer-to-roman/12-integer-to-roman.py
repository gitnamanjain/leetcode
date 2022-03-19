class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        rom = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        result=""
        for i in val:
            if num//i:
                count=num//i
                result+=rom[val.index(i)]*count
                num=num%i
        return result