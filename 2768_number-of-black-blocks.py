class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        """
        hashing

        time: O(c) where c is number of coordinates
        space: O(m * n) to store mapping between block to count
        """

        def is_out(i, j):
            return i < 0 or i >= m or j < 0 or j >= n

        # map block to count of black cells
        # block can be identified with the top left corner
        block_to_count = defaultdict(int)

        # for every black cell
        for x, y in coordinates:
            # check all possible blocks that can contain it

            # which blocks does a cell x, y belong in?
            # any one of these as long as its not the last row or column
            # x - 1, y - 1
            # x - 1, y
            # x, y - 1
            # x, y
            
            for i in [x - 1, x]:
                for j in [y - 1, y]:
                    if is_out(i, j):
                        continue
                    if i == m - 1 or j == n - 1:
                        # last row or column
                        continue
                    # increment count if valid block
                    block_to_count[(i, j)] += 1

        num_blocks_with_black = len(block_to_count)
        total_num_blocks = (m - 1) * (n - 1)
        blocks_with_zero = total_num_blocks - num_blocks_with_black

        res = [0] * 5
        res[0] = blocks_with_zero
        for block, count in block_to_count.items():
            res[count] += 1

        return res
        
