import os

extensions = {".jpg", ".jpeg", ".png", ".webp"}

files = [
    f for f in os.listdir(".")
    if os.path.isfile(f) and os.path.splitext(f)[1].lower() in extensions
]

files.sort()

for index, filename in enumerate(files, start=1):
    ext = os.path.splitext(filename)[1].lower()
    new_name = f"{index}{ext}"
    
    os.rename(filename, new_name)
    print(f"{filename} -> {new_name}")

print("Done.")