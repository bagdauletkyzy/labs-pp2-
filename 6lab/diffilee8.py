import os

path="/Users/akbotabagdauletkyzy/Desktop/row.txt"

if os.path.exists(path):
    os.remove(path)
    print("deleted")
else:
    print("Does not exist")
