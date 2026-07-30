class Solution:
    def isPalindrome(self, s: str) -> bool:
        array = [c.lower() for c in s if c.isalnum()]
        i = 0
        j = len(array) - 1
        while i < j:
            if array[i] != array[j]:
                return False
            i+=1
            j-=1
        return True
        