class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # to reduce time complexity: avoid O(m log m) sorting; use O(m) character counting instead
        # lists cannot be used as hashmap keys because they are mutable
        # keys must be immutable (like tuples) to be hashable
        hashmap = {} 
        for s in strs:
            alphabets = [0]*26
            for c in s:
                alphabets[ord(c) - ord('a')] += 1 # ord is a function that converts a character to a int
            key = tuple(alphabets)
            if key not in hashmap:
                hashmap[key] = [] # better to use a defaultdict
            hashmap[key].append(s)
            # converting to a tuple usually takes O(k) of time complexity depending on the size of the original array
            # but since the length of alphabets is fixed, it is considered O(1) here

        return list(hashmap.values())

        # time complexity: O(n*m) where n is the number of strings and m is the maximum length of a string in strs
        # space complexity: O(n*m)


    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # make a hash map
        # sort the string to make a unique key for each anagram group
    
        hashmap = {}
        for s in strs:
            sorted_str = ''.join(sorted(s)) # ''.join(list): list → str
            if sorted_str not in hashmap:
                hashmap[sorted_str] = [] # alternative: use defaultdict
            # list append is O(1)
            hashmap[sorted_str].append(s)
            
        return list(hashmap.values())
        
        # time complexity: O(n*mlogm) where n is the number of strings and m is the maximum length of a string in strs
        # space complexity: O(n*m)
        
        # space complexity analysis:
        # - numeric types (int/float) take O(1) space due to fixed memory allocation.
        # - strings take O(m) space because they are stored as sequences of 'm' individual characters.