# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

class Solution(object):
    def showRows(self, numRows):
        # Input: integer
        # Output: list of lists
        # Returns the first numRows of Pascal's triangle

        # base case: if numRows is 1 or 2 
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1, 1]]

        # iterate over previous row (numRows - 1) and calculate interior numbers of new array
        output = self.showRows(numRows - 1)
        prevRow = output[-1]
        curRow = []
        for i in range(1, len(prevRow)):
            curRow.append(prevRow[i] + prevRow[i - 1])

        # add 1s to each end of curRow
        curRow.insert(0, 1)
        curRow.append(1)

        # append array to result of numRows - 1 and return
        output.append(curRow)
        
        return output


def assertEqual(actual, expected):
    if actual == expected:
        print('passed')
    else:
        print(f'failed. expected {expected} but got {actual}')

assertEqual(Solution().showRows(3), [[1],[1,1],[1,2,1]])
assertEqual(Solution().showRows(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
