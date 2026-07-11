class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:   
        Pair = {}

        for char in strs:
            key = "".join(sorted(char))

            if key not in Pair:
                Pair[key] = []

            Pair[key].append(char)

        return list(Pair.values())