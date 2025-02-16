import re

with open('C:/Users/eradi/Desktop/pp2/pp2-labs/lab05/row.txt', 'r', encoding='utf-8') as f:
    row = f.read()
    
print(row)

# 1
res = re.findall(r'a[b]*', row)
print(res)

# 2
res = re.findall(r'ab{2,3}', row)
print(res)

# 3
res = re.findall(r'[a-z]+(_[a-z]+)+', row)
print(res)

# 4
res = re.findall(r'[A-Z][a-z]+', row)
print(res)

# 5
res = re.findall(r'a.*b$', row)
print(res)

# 6
res = re.sub(r'[\s,.]', ':', row)
print(res)

# 7
camel_str = ''.join(word.capitalize() if i != 0 else word for i, word in enumerate(row.split('_')))
print(camel_str)


# 8
result = re.split(r'(?=[A-Z])', row)
esult = [part for part in result if part]
print(result)

# 9
res = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ',row)
print(res)

# 10
snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', row).lower()
print(snake_str)