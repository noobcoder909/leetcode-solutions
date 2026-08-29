class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq=defaultdict(int)
        for i in s:
            freq[i]+=1
            if freq[i]>1:
                return i
        
            
        