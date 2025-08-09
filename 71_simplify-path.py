class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Return the simplified canonical path.
        
        given absolute path
            always starts with /
            consecutive slash //, ///, etc are treated as /
            . -> cur
            .. -> prev
            ... and more -> valid directory/file names
        
        canonical path
            starts with /
            directories separated with one /
            path must not end with a slash unless root directory
            no . or .. 

        Stack
        time: O(n)
        space: O(n)
        """
        
        # stack problem

        # split by /
        # for each item in stack
            # remove leading and trailing / (replace with white space, then call trim?)
            # use string.strip('/')
            # don't add . or empty string to stack
            # pop from stack when .. encountered
            # else, add to stack
        # at the end, join stack with '/' separating elements and add leading /

        stack = []
        trimmed_path = path.strip('/')
        path_list = trimmed_path.split('/')
        for item in path_list:
            cleaned_item = item.strip('/')
            if cleaned_item == '.' or cleaned_item == "":
                continue
            if cleaned_item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(cleaned_item)
        
        return '/' + "/".join(stack)
