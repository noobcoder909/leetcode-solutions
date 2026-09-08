class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        else:
            qut=(n//1000)-1

            rem=n%1000
            num=(qut*1000)+rem
            return num+1
        