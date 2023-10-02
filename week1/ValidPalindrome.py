class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # make alphanumeric

        # palindrome function


        s = s.replace(" ", "")
        s = s.lower()

        new_s = ""
        
        for index, value in enumerate(s):
            if value.isalnum():
                new_s += value
        
        # two pointers 
        # put them at ends, if ever unequal return false, 
        # exit loop if ever cross each other paths
        # if ran through the string with ease, return True

        l = 0 
        r = len(new_s) - 1

        while l < r:
            if new_s[l] != new_s[r]:
                return False
            l+=1
            r-=1

        return True