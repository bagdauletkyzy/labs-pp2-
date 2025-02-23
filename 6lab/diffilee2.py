import os
def check_access(path):
    if not os.path.exists(path):
        print("Path doesn't exist")
        return

    print("Exists: True")

    if os.access(path, os.R_OK):
        print("Readable")
    else:
        print("Not readable")

    if os.access(path, os.W_OK):
        print("Writable")
    else:
        print("Not writable")

    if os.access(path, os.X_OK):
        print("Executable")
    else:
        print("Not executable")

if __name__=="__main__":
    path_ch="/Users/akbotabagdauletkyzy/Documents"  
