class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size_s1 = len(s1)
        size_s2 = len(s2)
        # if size of s1 is greather than s2 there is no answer
        if size_s1 > size_s2:
            return False
        # mapping alphabet letters for s1 and s2
        map_char_s1 = [0] * 26
        map_char_s2 = [0] * 26
        for i in range(0, size_s1):
            map_char_s1[ord(s1[i]) - ord('a')] += 1
            map_char_s2[ord(s2[i]) - ord('a')] += 1

        # mapping the rest of s2 string
        for j in range(0, size_s2 - size_s1):
            # if at this moment the frequency is the same you found the result true
            if map_char_s2 == map_char_s1:
                return True
            # The frequency of the letters in both strings must be the same so we add in the new position and subtract the last one
            map_char_s2[ord(s2[j + size_s1]) - ord('a')] += 1
            map_char_s2[ord(s2[j]) - ord('a')] -= 1
        if map_char_s2 == map_char_s1:
            return True
        return False

sol = Solution()

print(sol.checkInclusion("ab", "eidboaoo"))