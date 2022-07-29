class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_len = 0
        window_start = 0
        window_final = 0
        map_char = {}
        size_s = len(s)
        while((window_final < size_s)):
            if s[window_final] in map_char:
                window_start = max(map_char[s[window_final]], window_start)
            map_char[s[window_final]] = window_final + 1
            sub_len = max(sub_len, window_final - window_start + 1)
            window_final += 1
        return sub_len

if __name__=="__main__":
    s = "dvdf"
    sol = Solution()

    print(sol.lengthOfLongestSubstring(s))