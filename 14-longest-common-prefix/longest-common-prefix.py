class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       result=strs[0]
       for i in strs:
        while not i.startswith(result):
            result=result[:-1]

       return result
    