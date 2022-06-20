class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
    # Approach 1
    # O(n log(n)) time | O(n) space
        result = ""
        # map to store string char as value and index as keys
        maps = {}
        # iterate over string
        for index, char in enumerate(s):
            #if char is not in map
            if char not in maps:
                # then add to map as key being the index and value being the character
                maps[indices[index]] = char
        # sort the array to access the index in ascending order
        indices.sort()
        # iterate over the sorted list
        for i in range(len(indices)):
            # for each index in indixes, add to string according to the index we see in map.
            result += maps[indices[i]]
        return result