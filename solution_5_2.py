from timeit import default_timer
from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt


def nuc2number(matrix):
    encoding = str.maketrans('ATGC', '1234')

    converted_matrix = []
    for row in matrix:
        converted_row = []
        for element in row:
            converted_row.append(int(element.translate(encoding)))
        converted_matrix.append(converted_row)

    return converted_matrix


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def matrix_multiplication(matrix1, matrix2):
    def vector_multiplication(vec1, vec2):
        return [vec1[i] * vec2[i] for i in range(len(vec1))]

    result = []
    matrix2_T = transpose(matrix2)

    for row1 in matrix1:
        result_row = []
        for row2 in matrix2_T:
            result_row.append(sum(vector_multiplication(row1, row2)))
        result.append(result_row)

    return result


def cut_matrix(matrix, size):
    result = []
    for i in range(size):
        result.append(matrix[i][:size])

    return result


path = 'C:\\Users\\iomyaki\\Downloads\\'

with open(path + '5.2_MSA.txt') as fin:
    MSA = []
    for line in fin:
        MSA.append(list(line.rstrip()))

msa_to_num1, msa_to_num2 = nuc2number(MSA), nuc2number(MSA)

# processing the second matrix
msa_to_num2.reverse()
msa_to_num2_T = transpose(msa_to_num2)

# evaluation loop
times_selfmade = []
times_numpy = []
std_selfmade = []
std_numpy = []
max_time = 0
for dim in tqdm(range(2, len(MSA) + 1)):
    dim_times_selfmade = []
    dim_times_numpy = []
    for epoch in range(100):
        # self-made
        start = default_timer()
        matrix_multiplication(cut_matrix(msa_to_num1, dim), cut_matrix(msa_to_num2_T, dim))
        duration = default_timer() - start
        dim_times_selfmade.append(duration)

        # from numpy
        start = default_timer()
        np.matmul(cut_matrix(msa_to_num1, dim), cut_matrix(msa_to_num2_T, dim))
        duration = default_timer() - start
        dim_times_numpy.append(duration)

    times_selfmade.append(np.mean(dim_times_selfmade))
    times_numpy.append(np.mean(dim_times_numpy))
    std_selfmade.append(np.std(dim_times_selfmade, dtype=np.float64))
    std_numpy.append(np.std(dim_times_numpy, dtype=np.float64))
    max_time = max(max_time, times_selfmade[dim - 2], times_numpy[dim - 2])

# create the chart
self_made = plt.errorbar(x=range(2, 101), y=times_selfmade, yerr=std_selfmade, color='red')
numpy_made = plt.errorbar(x=range(2, 101), y=times_numpy, yerr=std_numpy, color='blue')

# add title, labels, tick marks, and legend
plt.title('Matrix multiplication: self-made vs. numpy')
plt.xlabel('Dimension (100 runs each)')
plt.ylabel('Time, s')
plt.xticks(np.arange(0, 110, 10))
plt.yticks(np.arange(0, max_time + 0.005, 0.005))
plt.legend((self_made[0], numpy_made[0]), ('self-made', 'numpy'))

# display chart
plt.show()

# the last subtask
print(msa_to_num2_T[0], msa_to_num2_T[-1], sep='\n')
