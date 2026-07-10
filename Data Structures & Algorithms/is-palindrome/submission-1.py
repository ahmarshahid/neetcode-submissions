class Solution:
    def isPalindrome(self, s: str) -> bool:
        revS = ''
        for r in s:
            if r.isalnum():
                revS += r.lower()
        return revS == revS[::-1]  
        