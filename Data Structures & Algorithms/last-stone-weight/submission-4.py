class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            j = stones.pop()
            i = stones.pop()

            if j != i:
                stones.append(j-i)
        if stones:
            return stones[0]
        else:
            return 0