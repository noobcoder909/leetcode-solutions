class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        
        while s:
            if len(s)<=3 and i>0:
                break
            if i>len(s)-3:
                break
            if s[i]+s[i+1]+s[i+2]=='abc':
                s=s[:i]+s[i+3:]
                i=0
            else:
                i+=1          
                  
        if s=="":
            return True
        else:
            return False
        