class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        c=[]
        j=""
        n=len(s)
        if len(s)!=len(t):
            return False
        else:
            
            for i in range (0,n):
                j=s[i]
                c.append(j)
                if j in t:
                    c.remove(j)
                    t.remove(j)


            
               
            if c!=[]:
                #print(c)
                return False
            else:
                return True
        