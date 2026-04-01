from typing import List
from collections import defaultdict

# O(m * n) solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for term in strs:
            count = [0] * 26

            for char in term:
                count[ord(char) - ord("a")] += 1
            
            count = tuple(count)

            if count in res:
                res[count].append(term)
            else:
                res[count] = [term]
        
        return list(res.values())

# O(m * nlogn) solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matches = defaultdict(list)
        for s in strs:
            matches["".join(sorted(s))].append(s)
        
        return list(matches.values())

# O(m * nlogn) solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_terms_map = {}
        for index, term in enumerate(strs):
            sorted_term = "".join(sorted(term))
            if sorted_term in sorted_terms_map:
                sorted_terms_map[sorted_term].append(index)
            else:
                sorted_terms_map[sorted_term] = [index]

        solution = []
        for index, value in sorted_terms_map.items():
            sub_terms_list = []
            for i in value:
                sub_terms_list.append(strs[i])
            solution.append(sub_terms_list)

        return solution