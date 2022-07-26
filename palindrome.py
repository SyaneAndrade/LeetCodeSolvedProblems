import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        print(s)

        return self.verifyPhrase(s)
        
    def verifyPhrase(self, s):
        print(s)
        if s == "":
            return True
        elif len(s) == 1:
            return True
        elif s[0] == s[-1]:
            s = s[1: :]
            s = s[: -1 :]
            return self.isPalindrome(s)
        else:
            return False
    
    def isPalindrome2(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while(i < j):
            while(i < j) and not s[i].isalnum():
                i += 1
            while(i < j) and  not s[j].isalnum():
                j -= 1
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

if __name__=='__main__':
    sol = Solution()
    s = "A man, a plan, a canal: Panama"
    isTrue = sol.isPalindrome2(s)
    print(isTrue)


