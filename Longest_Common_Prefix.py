class Solution(object):
    def longestCommonPrefix(self, strs):
        pre = strs[0]

        for words in strs[1:]:
            while not words.startswith(pre):
                pre = pre[:-1]
            if not pre:
                return ""
        return pre