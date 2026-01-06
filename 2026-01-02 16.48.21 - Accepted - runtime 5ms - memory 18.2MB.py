class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            smallest = min(s)
            return s.count(smallest)
        
        # Calculate f for all words and sort
        word_frequencies = sorted([f(w) for w in words])
        n = len(words)
        
        result = []
        for q in queries:
            q_freq = f(q)
            # Binary search for count of words with f > q_freq
            # Find first position where word_freq > q_freq
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if word_frequencies[mid] > q_freq:
                    right = mid
                else:
                    left = mid + 1
            result.append(n - left)
        
        return result