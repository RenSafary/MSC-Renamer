import os

def rename(path):
    k = 1
    for filename in sorted(os.listdir(path)):
        last_name = os.path.join(path, filename)
        new_name = os.path.join(path, f"Trak{k}.ogg")
        os.rename(last_name, new_name)
        k+=1