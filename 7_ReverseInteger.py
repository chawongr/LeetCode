class Solution:
    def reverse(self, x: int) -> int:
        rev,temp,ans=[],[],''
        x=str(x)
        for i in x:
            if i=='-':temp.append(i)
            else:rev.append(int(i))
        rev=list(reversed(rev))
        while len(rev)!=0:temp.append(rev.pop(0))
        for i in temp:
            ans+=str(i)
        if int(ans)>=-1*pow(2,31) and int(ans)<=pow(2,31)-1:return int(ans)
        else:return 0
