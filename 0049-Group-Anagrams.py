class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1
            key = tuple(counts)

            if key not in hashmap:
                hashmap[key] = []
            
            hashmap[key].append(word)
        
        return hashmap.values()