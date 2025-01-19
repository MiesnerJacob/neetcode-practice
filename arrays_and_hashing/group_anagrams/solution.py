from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matches = defaultdict(list)
        for s in strs:
            matches["".join(sorted(s))].append(s)
        
        return list(matches.values())