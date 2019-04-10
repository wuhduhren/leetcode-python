#https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)
        for s in strs:
            anagrams[''.join(sorted(s))].append(s)
        return anagrams.values()