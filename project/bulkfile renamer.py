import os

def files(dir):
    files = os.listdir(dir)
    n = 1
    new = "file"

    for file in files:
        newname = f"{new}{n}"  
        os.rename(os.path.join(dir, file), os.path.join(dir, newname))
        n += 1
    print("task done")

files(r"D:\New folder")