class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ""
        maps = {}
        for index, char in enumerate(s):
            if char not in maps:
                maps[indices[index]] = char
                print(maps)
        indices.sort()
        for i in range(len(indices)):
            result += maps[indices[i]]
        return result