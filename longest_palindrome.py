class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return(s)
        if len(''.join(set(s))) == 1:
            return(s)
        
        # get candidates
        
        longest = ''
        len_longest = 0
        
        for ii in range(len(s)):
            # in case of odd
            left, right = ii, ii
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len_longest:
                    longest = s[left:(right+1)]
                    len_longest = len(longest)
                left -= 1
                right += 1
                
            # in case of even
            left, right = ii, ii + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > len_longest:
                    longest = s[left:(right+1)]
                    len_longest = len(longest)
                left -= 1
                right += 1
                
        return(longest)