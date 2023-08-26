class Solution(object):
    def intToRoman(self, num):
        n = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        roman=[]
        for i in range(len(n)):
            if(num//n[i]!=0):          
                for j in range(num//n[i]):             
                    roman.append(sym[i])                     
                num-=(num//n[i])*(n[i])
        return ''.join(roman) 
