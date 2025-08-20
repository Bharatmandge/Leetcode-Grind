class Solution:
    def isValidSudoku(self, board):
        """
        LeetCode Problem: Valid Sudoku

        A Sudoku board is valid if:
        1. Each row contains the digits 1-9 without duplicates.
        2. Each column contains the digits 1-9 without duplicates.
        3. Each of the nine 3x3 sub-boxes contains the digits 1-9 without duplicates.

        Note: The board does not need to be solved or complete, 
        only checked for validity.

        Approach:
        - Use 3 lists of sets to track numbers we’ve seen:
          * row_sets[i] tracks numbers in row i
          * col_sets[j] tracks numbers in column j
          * box_sets[k] tracks numbers in each 3x3 box
        - While traversing the board:
          * If a number is already present in the respective row, col, or box → invalid
          * Otherwise, add the number to the sets
        - If no conflicts found → board is valid
        """

        # Initialize 9 sets for rows, columns, and boxes
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        # Traverse each cell in the 9x9 board
        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num != '.':  # Skip empty cells
                    # Map (i, j) to its 3x3 box index
                    box_index = (i // 3) * 3 + (j // 3)

                    # If number already seen in row, column, or box → invalid
                    if num in row_sets[i] or num in col_sets[j] or num in box_sets[box_index]:
                        return False

                    # Otherwise, mark number as seen
                    row_sets[i].add(num)
                    col_sets[j].add(num)
                    box_sets[box_index].add(num)

        # No violations → valid Sudoku
        return True
