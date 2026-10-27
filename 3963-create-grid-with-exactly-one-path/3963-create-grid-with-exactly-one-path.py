class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        h='#'
        d='.'
        ans=[]
        ans.append(n*d)
        for i in range (m-1):
            ans.append((n-1)*h+d)
        return ans

        