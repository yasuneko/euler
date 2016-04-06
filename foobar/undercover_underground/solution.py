import math

def combinations(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def permutations(n, k):
    return math.factorial(n) / math.factorial(n - k)

def answer(N, K):


    degree_matrix = [[0 for x in range(N)] for x in range(N)]

    for node in range(N):
        degree_matrix[node][node] = N - 1

    for row in degree_matrix:
        print row

    exit()

    if K == N - 1:
        return N ** (N - 2)
    else:
        max_k = (N * (N - 1)) / 2
        edge_count = combinations(N, 2)

        if K == max_k - (N - 1):
            return combinations(edge_count, K) - N
        elif K in range(max_k - (N - 2), max_k + 1):
            return combinations(edge_count, K)

    edge_count = combinations(N, 2)

    return combinations(edge_count, K)
'''
print combinations(2, 2)
print combinations(3, 2)
print combinations(4, 2)
print combinations(5, 2)
print combinations(6, 2)
print combinations(7, 2)
print combinations(8, 2)
print combinations(9, 2)
print combinations(10,2)
exit()
'''

print answer(5, 4)

exit()

for x in range(2, 10):
    for i in range(x - 1, ((x * (x - 1)) / 2) + 1):
        print x,",", str(i).zfill(2), ":", answer(x, i)

print answer(3, 2)
print answer(4, 3)
print answer(4, 4)
print answer(4, 5)
print answer(4, 6)

print answer(5, 4)

print answer(5, 10)
print answer(5, 9)
print answer(20,19)
