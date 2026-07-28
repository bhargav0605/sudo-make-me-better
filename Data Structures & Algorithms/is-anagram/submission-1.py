class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        result_s = ''.join(sorted(s))
        result_t = ''.join(sorted(t))

        for index, character in enumerate(result_s):

            if character != result_t[index]:
                return False

        return True