N = input()

# 방법1
# for i in range(1, len(N)+1):
#     print(N[-i], end='')

# 방법2
# reverse_s = ''
# for i in range(0, len(N)):
#     reverse_s = N[i] + reverse_s
# print(reverse_s)

# 방법3
# a = list(N)
# b = []
#
# for i in range(len(a)):
#     b.append(a.pop())
#
# b = ''.join(b)
# print(b)

# 방법4
# a = list(N)
#
# for idx in range(len(a) // 2):
#     a[idx], a[-idx-1] = a[-idx-1], a[idx]
#
# a = ''.join(a)
# print(a)