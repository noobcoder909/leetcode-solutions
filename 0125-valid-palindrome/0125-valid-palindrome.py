class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        s=s.lower()
        while left<=right:
            if s[left].isalnum()==False:
                left+=1
                continue
            if s[right].isalnum()==False:
                right-=1
                continue
            if s[left]!=s[right]:
                return False
            else:
                left+=1
                right-=1
        return True

        