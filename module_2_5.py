# Функции в Python.Функция с параметром.
def get_matrix(n, m, vale):
    result = []
    for i in range(n):
        result.append([])
        for j in range(m):
            result[i].append(vale)
    return result
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)