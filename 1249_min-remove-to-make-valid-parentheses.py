class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        all lowercase letters will be part of the solution
        since we want to minimize deletions, we should keep as many
        valid parantheses as possible

        iterate over string and append each char to res[],
        unless the char is a closed parentheses and there aren't any
        open parantheses to pair it with (which can be tracked
        with a stack)

        if theres any open parentheses at the end,
        replace them with empty strings

        having res as an [] makes it efficient to
        replace open parentheses

        time: O(n)
        space: O(n)
        """
        res = []
        stack = []

        for c in s:
            if c == "(":
                stack.append(len(res))
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    res.append("")
                    continue

            res.append(c)
        
        while stack:
            i = stack.pop()
            res[i] = ""

        return "".join(res)

