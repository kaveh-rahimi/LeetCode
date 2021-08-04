class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        neg_flag= False
        
        if x < 0:
            neg_flag= True
            x=-x
        while (x>0):
            a = x % 10
            rev = rev * 10 + a
            x = x // 10
        if neg_flag == True:
            rev =- rev 
            
        if rev <= -2**31 or rev >= 2**31-1 :
            return 0
        return rev