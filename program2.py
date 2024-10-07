class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store roman values
        roman_dict = {'I': 1, 
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
        
        # Initializing result to 0 (to prevent initial/residual garbage values in variable )
        total = 0
        
        # Traverse the string
        for i in range(len(s)):
            # If the current numeral is less than the next one, subtract its value
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                total -= roman_dict[s[i]]
            else:
                # Otherwise, add its value
                total += roman_dict[s[i]]
        
        return total
        
        
        pass
