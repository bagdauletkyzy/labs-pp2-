path="/Users/akbotabagdauletkyzy/Desktop/fruits.txt"
fruits=["Apple","Banana","Cherry"]

with open(path,'w',encoding='utf-8') as f:
    for fruit in fruits:
        f.write(fruit+"\n")
