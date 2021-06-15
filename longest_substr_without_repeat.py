class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_str = ''
        lastc = ''
        temp_str = ''
        
        for c in s:
            if c != lastc:
                if c not in temp_str:
                    temp_str += c
                else:
                    temp_str = temp_str[temp_str.find(c)+1:] + c
                    
            else:
                temp_str = c
   
            if len(temp_str) > len(long_str):
                long_str = temp_str

            lastc = c
            
        if len(long_str) == 0:
            long_str = lastc
        
        return(len(long_str))