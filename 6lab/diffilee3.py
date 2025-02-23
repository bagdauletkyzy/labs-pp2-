import os

path="/Users/akbotabagdauletkyzy/Desktop/row.txt"
if os.path.exists(path):
    print("Path exists:",path)
    print("Directory:",os.path.dirname(path))
    print("Filename:",os.path.basename(path))
else:
    print("Path does not exist")
