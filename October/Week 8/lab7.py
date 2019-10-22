# --------------------------------------
# CSCI 127, Lab 7
# October 17, 2017
# Anthony Louis Rosenblum
# --------------------------------------

def create_list(q,s,t):
    w = sorted(q)
    value_list = []
    matrix_list = []
    for i in range(t):
        value_list.append(0)
    for i in range(s):
        matrix_list.append(value_list[:])
    for i in w:
        matrix_list[i[0]][i[1]] = q[i]
    return matrix_list

def print_matrix(m,r,c,s):
    matrix_list = create_list(m,r,c)
    print(s)
    print("")
    print_header(c)
    for i in range(r):
        for z in range(c):
            if matrix_list[i][z] >= 0:
                print("|  " + str(matrix_list[i][z]), end="")
            elif  matrix_list[i][z] < 0:
                print("| " + str(matrix_list[i][z]), end="")
        print("|")
        print_header(c)
    print("")
    return(matrix_list)

def add_lists(x,y):
    return [[sum(z) for z in zip(*w)] for w in zip(x,y)]

def add_matrices(x,y,r,c):
    matrix_1 = create_list(x,r,c)
    matrix_2 = create_list(y,r,c)
    matrix_3 = add_lists(matrix_1,matrix_2)
    output = {}
    for i in range(len(matrix_3)):
        for z in range(len(matrix_3[i])):
            output[(i,z)] = matrix_3[i][z]
    return(output)
    
# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def print_header(columns):
    line = "+"
    for i in range(columns):
        line += "---+"
    print(line)

# --------------------------------------

def read_matrix(input_file):
    matrix = {}
    line = input_file.readline().split()
    while line[0] != "stop":
        row = int(line[0])
        column = int(line[1])
        value = int(line[2])
        matrix[(row, column)] = value
        line = input_file.readline().split()
    return matrix

# --------------------------------------

def main (file_name):
    input_file = open(file_name, "r")
    
    line = input_file.readline().split()
    rows = int(line[0])
    columns = int(line[1])

    matrix_1 = read_matrix(input_file)
    print_matrix(matrix_1, rows, columns, "Matrix 1")
    
    matrix_2 = read_matrix(input_file)
    print_matrix(matrix_2, rows, columns, "Matrix 2")

    matrix_3 = add_matrices(matrix_1, matrix_2, rows, columns)
    print_matrix(matrix_3, rows, columns, "Matrix 1 + Matrix 2")
    print("Matrix 3 =", matrix_3)

# --------------------------------------

main ("sparse-matrix.txt")
