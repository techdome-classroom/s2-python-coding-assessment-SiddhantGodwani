class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary roman map to store Roman numeral values
        roman_dict = {'I': 1, 
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
        
        # Initialize result to 0 (to prevent initial/residual garbage values )
        total = 0
        
        # Traverse the string
        for i in range(len(s)):
            # If the current numeral is less than the next one, subtract its value
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                # Otherwise, add its value
                total += roman_map[s[i]]
        
        return total
        
        
        pass
