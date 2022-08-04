"""This solution works but it is really slow and uses up a ton of memory"""

class Solution(object):
    def isValid(self, s):
        """s: string -> boolean
        returns True if string is valid sequence of parantheses"""
        
        # d = {"{":"}", "(":")", "[":"]"}
        # print(s)
        d = {"}":"{", ")":"(", "]":"["}
        
        # Convert string to list
        L = list(s)
        
        while len(L) > 2:
            
            # print(L)
            
            # Loop through list
            temp = []
            for i in range(1, len(L)):
                
                # If closed parantheses is found and previous is matching
                if L[i] in d.keys() and L[i-1] == d[L[i]]:
                    
                    # Save indices
                    temp += [i-1, i]
            
            # print(temp)
            
            # Remove elements by saved indices
            for j in reversed(temp):
                del L[j]

            # print(L)
                
            # Repeat with shorter list until list length is below 2
                        
        # Convert list back to string
        s = ''.join(L)
        
        # If string is empty or matches any valid parentheses, return True
        if len(s) == 0 or s in ["()", "{}", "[]"]:
            return True
        
        return False


solution = Solution()
print(solution.isValid("[]{}"))
print(solution.isValid("[(){}]()"))
print(solution.isValid("[({})]"))
print(solution.isValid("[()()][(){}]"))
print(solution.isValid("[(){}](("))
print(solution.isValid("[(){}]()("))


#%%

class Solution1(object):
    def isValid(self, s):
        """s: string -> boolean
        returns True if string is valid sequence of parantheses"""
        
        # d = {"{":"}", "(":")", "[":"]"}
        # print(s)
        d = {"}":"{", ")":"(", "]":"["}
        
        # Base case is if len(s) <= 2 and is (), {}, or []
        if len(s) <= 2 and s in ["()", "{}", "[]"]:
            return True
        
        # Convert string to list
        L = list(s)

        # Iterate over list
        for i in range(1, len(L)):
            # print(i)
            # When a closed parantheses is found, if previous parantheses matches, delete both
            if L[i] in d.keys():
                if L[i-1] == d[L[i]]:
                    # Delete both and call function again with new list
                    del L[i-1:i+1]                  
                    return self.isValid(''.join(L))
        
        return False
    
#%%
"""The solution is faster and uses a lot less memory

Try to see how this is different from mine, I think the idea is roughly the same"""

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        # Loop through string
        for char in s:
            # If character is closed parentheses
            if char in dict: 
                # If no open parentheses or does not match the previous open, return F
                if stack == [] or dict[char] != stack.pop(): 
                    return False
                 
            # If character is an open parentheses
            else: 
                stack.append(char) # Append to stack

        return stack == []
    
    
solution = Solution()
print(solution.isValid("[]{}"))
print(solution.isValid("[(){}]()"))
print(solution.isValid("[({})]"))
print(solution.isValid("[()()][(){}]"))
print(solution.isValid("[(){}](("))
print(solution.isValid("[(){}]()("))