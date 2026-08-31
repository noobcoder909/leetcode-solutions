class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        ans=[]
        alph=["a","b","c","d","e",'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in nums:
            Binary=bin(i)[2:]
            
            Binary=Binary[::-1]
            
            word=""
            for j in range (len(Binary)):
                if Binary[j]=="1" and j<=25:
                    word=alph[j]+word
                elif Binary[j]=="1" and j>25 :
                    word='zz'+word
            ans.append(word)
        return ans

        