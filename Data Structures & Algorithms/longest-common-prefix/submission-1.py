class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def myfunc(x):
            return len(x)
        strs.sort(key = myfunc)
        strs.reverse()
        for i, x in enumerate(strs):
            if len(x) > len(strs[-1]):
                strs[i] = x[:len(strs[-1])]
        while any(x != strs[-1] for x in strs[:-1]):
            strs = [x[:-1] for x in strs]
        return strs[-1]