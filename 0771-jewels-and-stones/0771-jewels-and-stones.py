class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j=set(jewels)
        cout=0
        for i in stones:
            if i in j:
                cout+=1
        return cout

        
        