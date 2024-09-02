# Дополнительное практическое задание по модулю.
import  random
tikets = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
cipher = random.choice(tikets)
para = []
print(cipher)
for i in range(1, cipher):
    for j in range (i+1, cipher):
        if cipher % (i + j) == 0:
            para.append((i, j))
print(para)