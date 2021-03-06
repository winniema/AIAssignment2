from cspbase import *

def enforce_gac(constraint_list):
    '''Input a list of constraint objects, each representing a constraint, then 
       enforce GAC on them pruning values from the variables in the scope of
       these constraints. Return False if a DWO is detected. Otherwise, return True. 
       The pruned values will be removed from the variable object's cur_domain.
       enforce_gac modifies the variable objects that are in the scope of
       the constraints passed to it.'''
    # Input is a list of Constraint Objects

    repeat = 1

    while repeat == 1:
        repeat = 0
        for i in range(len(constraint_list)):
            constraint = constraint_list[i]
            scope = constraint.scope
            for var_index in range(len(scope)):
                var = scope[var_index]
                curr_domain = var.curdom
                if not curr_domain:
                    return False
                for value in curr_domain:
                    if not constraint.has_support(var, value):
                        #delete value of variable domain
                        var.prune_value(value)
                        repeat = 1
    return True

def sudoku_enforce_gac_model_1(initial_sudoku_board):
    '''The input board is specified as a list of 9 lists. Each of the
       9 lists represents a row of the board. If a 0 is in the list it
       represents an empty cell. Otherwise if a number between 1--9 is
       in the list then this represents a pre-set board
       position. E.g., the board
    
       -------------------  
       | | |2| |9| | |6| |
       | |4| | | |1| | |8|
       | |7| |4|2| | | |3|
       |5| | | | | |3| | |
       | | |1| |6| |5| | |
       | | |3| | | | | |6|
       |1| | | |5|7| |4| |
       |6| | |9| | | |2| |
       | |2| | |8| |1| | |
       -------------------
       would be represented by the list of lists
       
       [[0,0,2,0,9,0,0,6,0],
       [0,4,0,0,0,1,0,0,8],
       [0,7,0,4,2,0,0,0,3],
       [5,0,0,0,0,0,3,0,0],
       [0,0,1,0,6,0,5,0,0],
       [0,0,3,0,0,0,0,0,6],
       [1,0,0,0,5,7,0,4,0],
       [6,0,0,9,0,0,0,2,0],
       [0,2,0,0,8,0,1,0,0]]
       
       
       In model_1 you should create a variable for each cell of the
       board, with domain equal to {1-9} if the board has a 0 at that
       position, and domain equal {i} if the board has a fixed number i
       at that cell. 
       
       Model_1 should create BINARY CONSTRAINTS OF NOT-EQUAL between all
       relevant variables (e.g., all pairs of variables in the same
       row, etc.), then invoke enforce_gac on those constraints. All of the
       constraints of Model_1 MUST BE binary constraints (i.e.,
       constraints whose scope includes two and only two variables).

       After creating all variables and constraints you can invoke
       your enforce_gac routine to obtain the GAC reduced current domains
       of the variables.
       
       The ouput should have the same layout as the input: a list of
       nine lists each representing a row of the board. However, now the
       numbers in the positions of the input list are to be replaced by
       LISTS which are the corresponding cell's pruned domain (current
       domain) AFTER gac has been performed.
       
       For example, if GAC failed to prune any values the output from
       the above input would result in an output would be: NOTE I HAVE
       PADDED OUT ALL OF THE LISTS WITH BLANKS SO THAT THEY LINE UP IN
       TO COLUMNS. Python would not output this list of lists in this
       format.
       
       
       [[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                2],[1,2,3,4,5,6,7,8,9],[                9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                6],[1,2,3,4,5,6,7,8,9]],
       [[1,2,3,4,5,6,7,8,9],[                4],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                1],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                8]],
       [[1,2,3,4,5,6,7,8,9],[                7],[1,2,3,4,5,6,7,8,9],[                4],[                2],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                3]],
       [[                5],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                3],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
       [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                1],[1,2,3,4,5,6,7,8,9],[                6],[1,2,3,4,5,6,7,8,9],[                5],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
       [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                3],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                6]],
       [[                1],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                5],[                7],[1,2,3,4,5,6,7,8,9],[                4],[1,2,3,4,5,6,7,8,9]],
       [[                6],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                2],[1,2,3,4,5,6,7,8,9]],
       [[1,2,3,4,5,6,7,8,9],[                2],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[                8],[1,2,3,4,5,6,7,8,9],[                1],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]]
       
       Of course, GAC would prune some variable domains SO THIS WOULD
       NOT BE the outputted list.
       
       '''

    rows = len(initial_sudoku_board)
    cols = len(initial_sudoku_board[0])
    all_constraints = []

    # Initializing new board
    sudoku_board, output_sudoku_board = initialize_new_boards()

    # Create Variables
    sudoku_board = create_variables_for_board(initial_sudoku_board, sudoku_board)

    # Create Constraints
    # Create the rows and column constraints first
    for i in range(9):
        for j in range(9):
            pivot_var = sudoku_board[i][j]

            k = j + 1
            while k < 9:
                other_var_row = sudoku_board[i][k]
                c_one = Constraint('winnie', [pivot_var, other_var_row])
                constraint_tuples = make_constraint_tuples_model_1(c_one)
                c_one.add_satisfying_tuples(constraint_tuples)
                k = k + 1
                all_constraints.append(c_one)

            l = i + 1
            while l < 9:
                other_var_col = sudoku_board[l][j]
                c_two = Constraint('winnie', [pivot_var, other_var_col])
                c_two.add_satisfying_tuples(make_constraint_tuples_model_1(c_two))
                l = l + 1
                all_constraints.append(c_two)

            if (i % 3) == 0:
                if (j % 3) == 0:
                    list_pos_tuple = [(i+1, j+2), (i+1, j+1), (i+2, j+2), (i+2, j+1)]
                    add_sat_tuples_model_1(sudoku_board, all_constraints, pivot_var, list_pos_tuple)
                elif (j % 3) == 1:
                    list_pos_tuple = [(i+1, j-1), (i+1, j+1), (i+2, j-1), (i+2, j+1)]
                    add_sat_tuples_model_1(sudoku_board, all_constraints, pivot_var, list_pos_tuple)
                else:
                    list_pos_tuple = [(i+1, j-1), (i+1, j-2), (i+2, j-1), (i+2, j-2)]
                    add_sat_tuples_model_1(sudoku_board, all_constraints, pivot_var, list_pos_tuple)

            elif (i % 3) == 1:
                if (j % 3) == 0:
                    list_pos_tuple = [(i+1, j+1), (i+1, j+2)]
                    add_sat_tuples_model_1(sudoku_board, all_constraints, pivot_var, list_pos_tuple)
                elif (j % 3) == 1:
                    list_pos_tuple = [(i+1, j+1), (i+1, j-1)]
                    add_sat_tuples_model_1(sudoku_board, all_constraints, pivot_var, list_pos_tuple)
                else:
                    list_pos_tuple = [(i+1, j-2), (i+1, j-1)]
                    add_sat_tuples_model_1(sudoku_board, all_constraints, pivot_var, list_pos_tuple)
    check = enforce_gac(all_constraints)
    if not check:
        print("Fatal Error: DWO detected")

    for i in range(rows):
        for j in range(cols):
            output_sudoku_board[i][j] = sudoku_board[i][j].curdom

    return output_sudoku_board


def initialize_new_boards():
    ''' Creates two 9 by 9 matrixes with all 0 elements.
    Returns: a tuple with the two boards'''

    sudoku_board = []
    output_sudoku_board = []
    for i in range(9):
        sudoku_board.append([])
        output_sudoku_board.append([])
        for j in range(9):
            sudoku_board[i].append(0)
            output_sudoku_board[i].append(0)

    return sudoku_board, output_sudoku_board


def create_variables_for_board(initial_sudoku_board, sudoku_board):
    '''Input:
        initial_sudoku_board: a 9 x 9 matrix, with a integer between 0-9 in each cell
        sudoku_board: empty 9 x 9 matrix (all 0 values)
    Returns:
        sudoku_board: A variable for each cell of the board,
        with domain equal to {1-9} if the board has a 0 at that
        position, and domain equal {i} if the board has a fixed number i
        at that cell.'''

    for i in range(9):
        for j in range(9):
            domain = [initial_sudoku_board[i][j]]
            if domain[0] == 0:
                domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            name = (i, j)
            variable = Variable(name, domain)
            sudoku_board[i][j] = variable

    return sudoku_board


def add_sat_tuples_model_1(board, all_constraints, pivot_var, list_pos_tuples):
    '''Inputs: (1) sudoku board (2) list of tuples representing
    positions which all_diff constraint needs to be generated'''

    for t in list_pos_tuples:
        x, y = t
        other_var = board[x][y]
        c = Constraint('winnie', [pivot_var, other_var])
        c.add_satisfying_tuples(make_constraint_tuples_model_1(c))
        all_constraints.append(c)
    return None

def make_constraint_tuples_model_1(constraint):
    'Generates an original list of constrain tuples for the two variables specifically for the sudoku game'
    list_tuples = []
    scope = constraint.scope # Given that the scope of each constraint is two variables

    var1 = scope[0]
    var2 = scope[1]

    for var1_value in var1.dom:
        for var2_value in var2.dom:
            if var1_value != var2_value:
                tuple = (var1_value, var2_value)
                list_tuples.append(tuple)

    return list_tuples

##############################

def sudoku_enforce_gac_model_2(initial_sudoku_board):
    '''This function takes the same input format (a list of 9 lists
    specifying the board, and generates the same format output as
    sudoku_enforce_gac_model_1.
    
    The variables of model_2 are the same as for model_1: a variable
    for each cell of the board, with domain equal to {1-9} if the
    board has a 0 at that position, and domain equal {i} if the board
    has a fixed number i at that cell.

    However, model_2 has different constraints. In particular, instead
    of binary non-equals constaints model_2 has 27 all-different
    constraints: all-different constraints for the variables in each
    of the 9 rows, 9 columns, and 9 sub-squares. Each of these
    constraints is over 9-variables (some of these variables will have
    a single value in their domain). model_2 should create these
    all-different constraints between the relevant variables, then
    invoke enforce_gac on those constraints.
    '''
    rows = len(initial_sudoku_board)
    cols = len(initial_sudoku_board[0])
    all_constraints = [] #List of constrain objects

    # Initializing new board
    sudoku_board, output_sudoku_board = initialize_new_boards()

    # Create Variables
    sudoku_board = create_variables_for_board(initial_sudoku_board, sudoku_board)

    # Create Constraints
    box_index = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

    for i in range(9):
        # Columns and rows
        scope_row = []
        scope_col = []
        for j in range(9):
            scope_row.append(sudoku_board[i][j])
            scope_col.append(sudoku_board[j][i])
        c_row = Constraint('Gustave', scope_row)
        c_col = Constraint('Zero', scope_col)
        tups_row = make_constraint_tuples_model_2(c_row)
        tups_col = make_constraint_tuples_model_2(c_col)
        c_row.add_satisfying_tuples(tups_row)
        c_col.add_satisfying_tuples(tups_col)
        all_constraints.append(c_row)
        all_constraints.append(c_col)

        # Boxes
        x, y = box_index[i]
        c_box = generate_box_constraint(sudoku_board, x, y)
        tups_box = make_constraint_tuples_model_2(c_box)
        c_box.add_satisfying_tuples(tups_box)
        all_constraints.append(c_box)

    check = enforce_gac(all_constraints)
    if not check:
        print("Fatal Error: DWO detected")

    # Generate proper return style, list of list (like input)
    for i in range(rows):
        for j in range(cols):
            output_sudoku_board[i][j] = sudoku_board[i][j].curdom
    return output_sudoku_board

def make_constraint_tuples_model_2(constraint):
    list_tuples = []
    c_scope = constraint.scope

    sat_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Look for values that have domain of 1
    taken_values = [] # Saves values that are taken
    index_zeros = [] # Saves the index of all variables whos domain is greated than 1

    for i in range(9):
        if c_scope[i].domain_size() == 1:
            sat_list[i] = c_scope[i].dom[0]
            taken_values.append(c_scope[i].dom[0])
        else:
            index_zeros.append(i)

    free_values = []
    for v in range(1, 10):
        if taken_values.count(v) == 0:
            free_values.append(v)

    sat_tuple = tuple(sat_list)
    permutation_list = permutate(free_values)

    for y in range(len(permutation_list)):
        perm_list = list(permutation_list[y])
        curr_sat_list = list(sat_tuple)
        for d in range(len(index_zeros)):
            curr_sat_list[index_zeros[d]] = perm_list[d]
        t = tuple(curr_sat_list)
        list_tuples.append(t)

    return list_tuples

def generate_box_constraint(board, x, y):
    scope_b = []
    for i in range(3):
        for j in range(3):
            scope_b.append(board[x+i][y+j])
    c_box = Constraint('Boy with Apple', scope_b)
    return c_box

def permutate(free_values):
    '''Returns a list of tuples'''

    permutations_list = []

    # Set up first tuple
    perm = free_values[0], # a tuple of a single value
    permutations_list.append(perm)

    for f in range(1, len(free_values)):
        curr_val = free_values[f]
        curr_len = len(permutations_list)

        if len(permutations_list[0]) == len(free_values):
            break
        for k in range(curr_len):
            curr_perm = permutations_list.pop(0)
            for p in range(len(curr_perm) + 1):
                working_perm = list(curr_perm)
                working_perm.insert(p, curr_val)
                working_perm_tup = tuple(working_perm)
                permutations_list.append(working_perm_tup)
            curr_len = len(permutations_list)

    return permutations_list