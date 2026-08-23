class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out=[]
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        n=len(freq)
        
        for i in range (k):
            maximum=0
            for k,v in freq.items():
                if v>maximum:
                    maximum=v
                    maxnum=k
            out.append(maxnum)
            del freq[maxnum]
        return out  
