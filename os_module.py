# using os to do things
import os

#echo to the terminal
# os.system('echo "Hello world')

#make and changes directories

# ~create a directory
# directory name
directory = "test_dir"
# parent dir name
parent_dir = "C:/Users/Mushahid"
#path
path = os.path.join(parent_dir, directory)

# create DIR

os.mkdir(path)

# putting a new file in the new dir

filename = "testfile.txt"
filepath = os.path.join(path, filename)

with open(filepath, "w") as file1:
    toFile = "contents of file is written here"
    file1.write(toFile)

print("file" + filename + "created in" + directory + "folder")





