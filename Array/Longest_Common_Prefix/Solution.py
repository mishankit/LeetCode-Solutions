class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in strs:
            while i[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                    
        return prefix

        