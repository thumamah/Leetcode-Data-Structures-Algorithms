class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
    # Technique: Split string
    # Brute Force approach
    # O(n) time | O(1) space
    
        maxWords = 0
        # iterate over sentences
        for sentence in range(len(sentences)):
            # store the amount of words of each sentence
            words = len(sentences[sentence].split())
            # store the max number of words of the sentences 
            maxWords = max(maxWords, words)
        
        return maxWords
        