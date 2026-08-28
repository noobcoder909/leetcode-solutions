class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)%2==1):
            return False
        else:
            stack=["null"]
            close={")":"(","]":"[","}":"{","null":"null"}
            for i in s:
                if i=="(" or i=="[" or i=="{":
                    stack.append(i)
                else:
                    t=close[i]
                    if stack[-1]==t:
                        temp=stack.pop()
                    else:
                        return False
        if stack==["null"]:
            return True
        else:
            return False
                
                


            