class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Creating a stack to keep track of opening brackets
        stack = []
        # Dictionary to map closing brackets to their corresponding opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        # Iterate through each character in the string
        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # Pop from stack if it's not empty, else assign a dummy value ie. "empty"
                top_element = stack.pop() if stack else '#'
                
                # Check if the popped "]" element matches the corresponding opening bracket "["
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it to the stack otherwised
                stack.append(char)
        
        # If the stack=empty(at the end), it means all brackets were matched properly by my code
        return not stack
        
        
        pass







    



  

