src="/Users/akbotabagdauletkyzy/Desktop/row.txt"
dst="/Users/akbotabagdauletkyzy/Desktop/copy.txt"

with open(src,'r',encoding='utf-8') as s, open(dst,'w',encoding='utf-8') as d:
    d.write(s.read())
