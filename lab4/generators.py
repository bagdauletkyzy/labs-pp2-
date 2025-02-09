# 1
def square(N):
    for i in range(N):
        yield i**2

# num = int(input())
# nums = square(num)

# j = 1
# for i in nums:
#     print(f'{j}^2 = {i}')
#     j += 1

# 2
def even_nums(n):
    for i in range(n):
        if i%2 == 0:
            yield i

# N = int(input('Enter the num: '))
# nums = even_nums(N)

# for i in nums:
#     print(i, end=' ')
            
# 3
def divisible_3_4(n):
    for i in range(n):
        if i%3 == 0 and i%4 == 0:
            yield i

# N = int(input('Enter the num: '))
# nums = divisible_3_4(N)

# for i in nums:
#     print(i, end=' ')
            
# 4
def squares(a, b):
    for i in range(a, b):
        yield i**2

# x, y = map(int, input().split())
# nums = squares(x, y)

# for i in nums:
#     if i%0.5 == 0:
#         print(f'{x}^2 = {i}')
#         x += 1
        
# 5
def nums_to_n(n):
    for i in range(n, 0, -1):
        yield i

# N = int(input('Enter the num: '))
# nums = nums_to_n(N)

# for i in nums:
#     print(i, end=' ')