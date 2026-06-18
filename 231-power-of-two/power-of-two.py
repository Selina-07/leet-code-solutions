class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c=0
        i='1'
        if n<=0:
            return False

        elif (n%2==0 or n==1):
            num=bin(n)[2:] 
            if i in num:
                c=num.count(i)
                if c==int('1'):
                    return True
                else:
                    return False
        else:
            return False

        