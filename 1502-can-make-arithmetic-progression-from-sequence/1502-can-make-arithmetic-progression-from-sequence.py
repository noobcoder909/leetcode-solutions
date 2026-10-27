class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        n = len(arr)

        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        diff=arr[1]-arr[0]
        for i in range (1,n):
            if arr[i]-arr[i-1]!=diff:
                return False
        return True

        