class Solution(object):
    def isPalindrome(object,  x):
        x = str(x)
        if len(x)==1:return True
        elif len(x)==2 and x[0]==x[-1]:return True
        elif x[0]==x[-1]:return Solution.isPalindrome(object,x[1:-1])
        else:return False
