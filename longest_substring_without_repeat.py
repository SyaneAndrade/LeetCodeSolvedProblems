from tkinter import SOLID


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pivot = ""
        sub_len = 0
        sum = 0
        map_char = {}
        for i in range(len(s)):
            if s[i] in map_char:
                sub_len = sub_len if sub_len > sum else sum
                i = i - 1
                sum = 0
                map_char={}
            sum += 1
            map_char[s[i]] = i + 1
        return sub_len if sub_len > sum else sum

if __name__=="__main__":
    s = "dvdf"
    # s = "aab"
    # s = "abcabcbb"
    sol = Solution()

    print(sol.lengthOfLongestSubstring(s))