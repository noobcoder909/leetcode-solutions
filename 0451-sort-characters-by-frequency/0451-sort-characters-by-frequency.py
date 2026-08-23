class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        
        out=""
        
        n=len(freq)
        print(freq)
        for i in range (n):
            maxk=None
            maximum=0
            for k,v in freq.items():
                if v>maximum:
                    maximum=v
                    maxk=k
            
            out=out+(maxk*maximum)
            del freq[maxk]
        return out


