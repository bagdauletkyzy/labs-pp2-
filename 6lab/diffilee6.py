import string

path="/Users/akbotabagdauletkyzy/Desktop/"

for letter in string.ascii_uppercase:
    with open(f"{path}{letter}.txt", "w", encoding="utf-8") as f:
        f.write(f"This is {letter}.txt\n")
