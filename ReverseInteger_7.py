class Solution:
    def reverse(self, x: int) -> int:
        rev,temp=[],[]
        x=str(x)
        for i in x:
            if i=='-':
                temp.append(i)
            else:
                rev.append(int(i))
        rev=list(reversed(rev))
        while len(rev)!=0:
            temp.append(rev.pop(0))
        ans=''
        for i in temp:
            ans+=str(i)
        if int(ans)>=-2147483648 and int(ans)<=2147483647:
            return int(ans)
        else:
            return 0
