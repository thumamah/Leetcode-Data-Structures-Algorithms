class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
    # Brute Force approach
    # O(n) time | O(1) space
    
        maxWords = 0
        for sentence in range(len(sentences)):
            words = len(sentences[sentence].split())
            maxWords = max(maxWords, words)
        return maxWords
        