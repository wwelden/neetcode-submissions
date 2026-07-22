class Solution:
    def isPalindrome(self, s: str) -> bool:
       newS = ""

       for c in s:
            if c.isalnum():
                newS += c.lower()

       length = len(newS)

       for i in range(length):
            if newS[i] != newS[length-i-1]:
                return False
            if i == length-i-1:
                return True    
        
       return True