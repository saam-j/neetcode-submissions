
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        anagram_map=defaultdict(list)
        for s in strs:
            sorted_s=tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        for i in anagram_map.values():
            result.append(i)
        return result


