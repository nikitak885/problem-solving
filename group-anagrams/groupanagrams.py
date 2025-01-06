from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
ts = Solution()
listone = ["act","pots","tops","cat","stop","niki"]
val = ts.groupAnagrams(listone)
print("the sum of two list index are:",val)