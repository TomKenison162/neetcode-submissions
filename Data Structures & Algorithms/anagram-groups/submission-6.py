class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups = defaultdict(list
        )
        for w in strs:
            groups[tuple(sorted(w))].append(w)     # tuple: hashable
        return list(groups.values())



