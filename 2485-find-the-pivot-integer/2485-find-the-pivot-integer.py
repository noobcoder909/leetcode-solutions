class Solution:
    def pivotInteger(self, n: int) -> int:
        left=0
        right=n
        lsum=0
        rsum=n
        while (left!=right):
            if lsum<=rsum:
                left+=1
                lsum+=left
            elif lsum>rsum:
                right-=1
                rsum+=right
        if lsum==rsum:
            return left
        else:
            return -1

        