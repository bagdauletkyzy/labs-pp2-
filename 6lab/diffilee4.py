path="/Users/akbotabagdauletkyzy/Desktop/row.txt"

with open(path, 'r', encoding='utf-8') as f:
    print("Num:", len(f.readlines()))
