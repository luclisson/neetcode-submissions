class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            plan:
            for each int 0-9 create two hash maps
                - one for colums uniqueness
                - one for rows uniqueness
                - one for 3x3 boxes
                    0-2 row, 0-2 col = 0
                    0-2 row, 3-5 col = 1 ...
                    (row index // 3 * 3) + col index //3
                    indexing boxes
        """

        out_h_map = {}
        """
            build hashmap (could also be array)
            int: (rows_unique hashmap,
                   cols_unique hashmap)
        """
        for ind_r,row in enumerate(board):
            for ind_c,cell in enumerate(row):
                if cell != "." and cell in out_h_map:
                    row_h_map,col_h_map,box_h_map = out_h_map.get(cell)
                    if ind_r in row_h_map:
                        row_h_map[ind_r] = row_h_map.get(ind_r)+ 1
                    else: row_h_map[ind_r] = 1

                    if ind_c in col_h_map:
                        col_h_map[ind_c] = col_h_map.get(ind_c)+ 1
                    else: col_h_map[ind_c] = 1

                    box_ind = (ind_r // 3 * 3) + (ind_c // 3)
                    if box_ind in box_h_map:
                        box_h_map[box_ind] = box_h_map.get(box_ind) + 1
                    else: box_h_map[box_ind] = 1
                
                else: 
                    box_ind = (ind_r // 3 * 3) + (ind_c // 3)
                    out_h_map[cell] = ({ind_r:1},{ind_c:1},{box_ind:1})

        #check rows, cols and boxes are valid
        for rows_map,col_map,box_map in out_h_map.values():
            if (
            max(rows_map.values())>1 or
            max(col_map.values())>1 or
            max(box_map.values())>1
            ):
                return False
        return True
 