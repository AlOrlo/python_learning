from typing import List


def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    #create a function to calculate inner multiplication table
    def mult_table(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
        #create epmty list
        mult_table = [[] for i in range(row_end - row_start + 1)]
        #calculating multiplication
        for rows in range(len(mult_table)):
            for columns in range(column_start, column_end + 1):
                if columns == 0:
                    mult_table[rows].append(row_start + row)
                else:
                    mult_table[rows].append(columns * (row_start + rows))
        return mult_table


    # #create a full list of multiplication table
    # def full_table(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    #     #create zero row as headings
    #     row_zero = [i for i in range(column_start, column_end + 1, 1)]
    #     row_zero.insert(0, ' ')
    #     mt_full = mult_table(row_start, row_end, column_start, column_end)
    #     for i in range(len(mt_full)):
    #         mt_full[i].insert(0, row_start + i)
    #     mt_full.insert(0, row_zero)
    #     return mt_full


    return mult_table(row_start, row_end, column_start, column_end)  #, '\n',
            #'that is equal to the following multiplication table:', '\n',
            #full_table(row_start, row_end, column_start, column_end))