import os

path = input("Enter directory path: ")

# get list of files in the directory
files = os.listdir(path)

# sort the files by name
files.sort()

# loop through the files and rename them in ascending numerical order
count = 1
for file in files:
    if os.path.isfile(os.path.join(path, file)):
        filename, ext = os.path.splitext(file)
        new_filename = str(count).zfill(3) + ext
        os.rename(os.path.join(path, file), os.path.join(path, new_filename))
        count += 1
