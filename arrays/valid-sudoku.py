from collections import defaultdict


class Solution:
    def isValidSudoku(self, board):
        cols = defaultdict(set) # int -> set # 9 cols (0-8)
        rows = defaultdict(set) # int -> set # 9 rows (0-8)
        boxes = defaultdict(set) # (r//3, c//3) -> set # 9 boxes [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
        
        for r in range(9):
            for c in range(9):
                elem = board[r][c]
                if elem == ".":
                    continue
                if (
                    elem in rows[r] or 
                    elem in cols[c] or 
                    elem in boxes[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(elem)
                rows[r].add(elem)
                boxes[(r // 3, c // 3)].add(elem)
        return True
    
print(
    Solution().isValidSudoku(
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    )
)
                    
                     
                
                










class Solution_brute_force:
    
    def validate_all_rows(self, board):
        count = 0
        distinct = set()
        for row in board:
            empty_ele_cnt = 0
            distinct.clear() # new empty set for every row
            for element in row:
                if element == '.':
                    empty_ele_cnt += 1
                elif element not in distinct:
                    distinct.add(element)
            if empty_ele_cnt + len(distinct) == 9:
                count += 1
        return count
    
    def validate_all_cols(self, board):
        count = 0
        distinct = set()
        for j in range(9):
            empty_ele_cnt = 0
            distinct.clear() # new empty set for every col
            for i in range(9):
                element = board[i][j]
                if element == '.':
                    empty_ele_cnt += 1
                elif element not in distinct:
                    distinct.add(element)
            if empty_ele_cnt + len(distinct) == 9:
                count += 1
        return count
    
    def validate_all_sub_boxes(self, board):
        # how do i search in every 3x3 box
        count = 0
        distinct = set()
        
        # there are 9 (3x3)-boxes, and 3 box_rows
        # box_rows = 3
        # for row in range(box_rows):
        #     # each row has 3 boxes
        #     boxes = 3
        #     for box in range(boxes):
        #         i, i_lim = box*3, box*3 + 3 # to traverse in row when col is constant
        #         j, j_lim = box_rows*3, box_rows + 3 # to change column
        #         empty_ele_cnt = 0
        #         distinct.clear() # new empty set for every box
        #         # checking every element in the box
        #         while j < j_lim:
        #             while i < i_lim:
        #                 ###
        #                 element = board[i][j]
        #                 if element == '.':
        #                     empty_ele_cnt += 1
        #                 elif element not in distinct:
        #                     distinct.add(element)
        #                 ###
        #                 i+=1
        #             j+=1
        #         # completed cheking a box
        #         if empty_ele_cnt + len(distinct) == 9:
        #             count += 1
                

    def isValidSudoku_bruteforce(self, board) -> bool:
        count = 1
        count += self.validate_all_rows(board)
        count += self.validate_all_cols(board)
        count += self.validate_all_sub_boxes(board)
        return count == 27