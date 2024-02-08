import os
#  if you have backslashes(\) in your file path, you'll probably need double backslashes(\\), 
#  because that's escape seqences for a backslash within a string 
path = "D:\\builds\\codding\\python\\file"

# if os.path.exists(path):
#     print("Location exits in Disk", path[:2])
#     if os.path.isfile(path):
#         print(":) that is a file")
#     elif os.path.isdir(path):
#         print("That is directory!")
# else:
#     print("location don't exits!")

#  ** read file
# try:
#     with open("./file/text.tx") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("that file was not found :(")

#  ** write file w = write, r = read

# text = "this text has beem overwritten\n"
# text2 = "Have a nice day! See ya\n the above text has been appended here!"

# try:
#     with open("./file/text3.txt", "a") as file:
#         file.write(text + text2)
# except: Exception

# **copying conntet of file we use **shutil module that has 3 methods
# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metaData(file's creation and modification times)


import shutil
# shutil.copyfile('./file/test.txt', "./file/copy.txt") #(src, dest) arguments same but you can use any methods depening on your use

 # **move a file
# source = "folder"
# destination = "D:\\builds\\codding\\python\\file\\folder"

# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source, destination)
#         print(source + " was moved")
# except FileNotFoundError:
#     print(source + " was not found ")


# **delete a file
tempPath = "./file/temp.txt"
empty_folder_path ="./empty_folder"
try:
    # os.remove(empty_folder_path)   # delete a file
    # os.rmdir(empty_folder_path)    # delete an empty directory
    # shutil.rmtree(empty_folder_path)  # delete a directory containing files
    
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You can not delete using that function")
else:
    print(empty_folder_path + "was deleted")
