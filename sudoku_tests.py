from sudoku_csp_cyn import *

b1 = [[0,0,2,0,9,0,0,6,0],
     [0,4,0,0,0,1,0,0,8],
     [0,7,0,4,2,0,0,0,3],
     [5,0,0,0,0,0,3,0,0],
     [0,0,1,0,6,0,5,0,0],
     [0,0,3,0,0,0,0,0,6],
     [1,0,0,0,5,7,0,4,0],
     [6,0,0,9,0,0,0,2,0],
     [0,2,0,0,8,0,1,0,0]]


b2 = [[1,0,6,0,8,0,3,0,0],
      [0,9,7,4,0,1,0,0,0],
      [0,5,0,3,0,0,7,0,0],
      [4,0,0,0,0,7,0,6,0],
      [2,0,0,0,0,0,0,0,8],
      [0,7,0,5,0,0,0,0,9],
      [0,0,3,0,0,9,0,1,0],
      [0,0,0,2,0,3,8,5,0],
      [0,0,8,0,6,0,9,0,4]]


b3 = [[0,7,0,8,5,0,0,0,0],
      [0,9,0,0,0,1,5,0,6],
      [0,0,0,3,0,0,4,0,0],
      [0,3,0,0,0,0,0,0,8],
      [1,0,5,0,0,0,7,0,3],
      [7,0,0,0,0,0,0,2,0],
      [0,0,1,0,0,6,0,0,0],
      [2,0,3,7,0,0,0,6,0],
      [0,0,0,0,3,2,0,1,0]]


b4 = [[0, 0, 0, 0, 0, 6, 0, 0, 0],
      [0, 0, 0, 4, 0, 0, 2, 0, 8],
      [6, 3, 7, 0, 0, 8, 0, 0, 0],
      [2, 4, 0, 0, 0, 0, 0, 9, 0],
      [0, 0, 0, 9, 1, 7, 0, 0, 0],
      [0, 7, 0, 0, 0, 0, 0, 1, 3],
      [0, 0, 0, 3, 0, 0, 6, 8, 1],
      [1, 0, 4, 0, 0, 9, 0, 0, 0],
      [0, 0, 0, 8, 0, 0, 0, 0, 0]]

b5 = [[0, 6, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 7, 0, 0, 0, 0, 0, 4],
      [0, 9, 3, 0, 7, 0, 0, 0, 2],
      [0, 0, 1, 6, 0, 0, 0, 0, 5],
      [0, 0, 0, 8, 4, 2, 0, 0, 0],
      [3, 0, 0, 0, 0, 7, 8, 0, 0],
      [6, 0, 0, 0, 9, 0, 3, 1, 0],
      [7, 0, 0, 0, 0, 0, 5, 0, 0],
      [0, 0, 0, 0, 0, 5, 0, 9, 0]]

b6 = [[7, 0, 0, 1, 6, 0, 0, 0, 0],
      [3, 0, 0, 9, 0, 0, 0, 6, 0],
      [0, 0, 0, 8, 0, 0, 9, 2, 0],
      [0, 0, 6, 0, 1, 0, 0, 5, 0],
      [9, 0, 0, 0, 0, 0, 0, 0, 6],
      [0, 2, 0, 0, 3, 0, 7, 0, 0],
      [0, 1, 3, 0, 0, 2, 0, 0, 0],
      [0, 6, 0, 0, 0, 4, 0, 0, 8],
      [0, 0, 0, 0, 9, 1, 0, 0, 5]]

b7 = [[0, 9, 4, 3, 0, 0, 0, 0, 0],
      [0, 0, 7, 5, 0, 0, 0, 0, 0],
      [0, 0, 1, 4, 0, 0, 0, 2, 0],
      [4, 6, 0, 8, 0, 0, 0, 0, 3],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [2, 0, 0, 0, 0, 3, 0, 6, 9],
      [0, 5, 0, 0, 0, 6, 2, 0, 0],
      [0, 0, 0, 0, 0, 5, 1, 0, 0],
      [0, 0, 0, 0, 0, 1, 6, 4, 0]]

b8 = [[0, 9, 4, 3, 0, 0, 0, 0, 0],
      [0, 9, 7, 5, 0, 0, 0, 0, 0],
      [0, 0, 1, 4, 0, 0, 0, 2, 0],
      [4, 6, 0, 8, 0, 0, 0, 0, 3],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [2, 0, 0, 0, 0, 3, 0, 6, 9],
      [0, 5, 0, 0, 0, 6, 2, 0, 0],
      [0, 0, 0, 0, 0, 5, 1, 0, 0],
      [0, 0, 0, 0, 0, 1, 6, 4, 0]]

if __name__ == '__main__':
    #boards = [b1, b2, b3, b4, b5, b6, b7]
    boards = [b1]
    for b in boards:
        print("Solving board m{}".format(boards.index(b)))
        for row in b:
            print(row)
        print("--------------------------------------------")
        print("GAC reduced domains from MODEL 1")
        sol1 = sudoku_enforce_gac_model_1(b)
        for row in sol1:
            print(row)

        # TODO: I had to add brackets to the print statements, is that okay?
        '''
        print("GAC reduced domains from MODEL 2")
        sol2 = sudoku_enforce_gac_model_2(b)
        for row in sol2:
            print(row)
        print("============================================")
        '''