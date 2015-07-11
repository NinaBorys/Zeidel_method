#! /usr/bin/python
import copy


def Zeidel_iteration(matrix, rightCol, inputVector):
    result = [None] * len(inputVector)
    for i, k in enumerate(rightCol):
        result[i] = rightCol[i]
        for j, k in enumerate(rightCol):
            result[i] += matrix[i][j] * \
                inputVector[j] if i <= j else matrix[i][j] * result[j]
    return result


def Zeidel_met(matrix, rightCol, vector, epselon):
    readyMatrix, readyCol = prepare_matrix(matrix, rightCol)
    i = 0
    while True:
        vectorNew = Zeidel_iteration(readyMatrix, readyCol, vector)
        i += 1
        if i < 4:
            print("{0}\t{1}\t{2}".format(
                i, [round(x, 4) for x in vector], round(exit_test(vector, vectorNew), 4)))
        if exit_test(vector, vectorNew) < epselon:
            break
        vector = vectorNew
    print("\n{0}\t{1}".format(i, [round(x, 4) for x in vector]))


def exit_test(vector1, vector2):
    return max([abs(k - v) for k, v in zip(vector1, vector2)])


def prepare_matrix(matrix, rightCol):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                matrix[i][j] /= - matrix[i][i]
        rightCol[i] /= matrix[i][i]
        matrix[i][i] = 0
    return matrix, rightCol


def main():
    print(
        "NCM: Assignment #3: Solving systems of linear equations (iterations methods) \n")

    epselon = 0.0001
    matrix_A = [[8.30, 2.62, 4.10, 1.90],
                [3.92, 8.45, 8.78, 2.46],
                [3.77, 7.21, 8.04, 2.28],
                [2.21, 3.65, 1.69, 6.99]]

    matrix_A_diag = [[8.15, 1.38, 3.36, 1.72],
                     [0.15, 1.24, 0.74, 0.18],
                     [0.159, 4.872, 5.234, -0.054],
                     [4.59, 2.42, 18.62, -39.65]]

    matrix_C = [[103.353, 90.118, 102.493, 49.457],
                [90.118, 143.573, 149.070, 67.717],
                [102.493, 149.070, 161.396, 59.533],
                [49.457, 67.717, 59.533, 63.720]]

    b = [-10.65,
         12.21,
         15.45,
         -8.35]

    b_diag = [-7.41,
              -3.24,
              15.605,
              84.43]

    d = [-0.7388,
         156.1885,
         173.6453,
         -13.3389]

    start_vector = [1, 1, 1, 1]

    print("for system with diagonal dominance: \n")
    Zeidel_met(copy.deepcopy(matrix_A_diag), copy.deepcopy(
        b_diag), copy.deepcopy(start_vector), epselon)

    print("\n for multiplied on transposed matrix: \n")
    Zeidel_met(matrix_C, d, start_vector, epselon)


if __name__ == '__main__':
    main()
