import os

def rename_files():
    # Get file names
    file_list = os.listdir("/home/sango/Downloads/prank")
    # print(file_list);
    saved_path = os.getcwd()
    os.chdir("/home/sango/Downloads/prank")
    # For each file, rename filename
    for file_name in file_list:
        print("Old name -" +file_name);
        print("New name -" +file_name.translate(None, "0123456789"));
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files()
