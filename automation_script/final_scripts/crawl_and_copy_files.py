import os, shutil
#from utils.stringUtils import massage_directory_path 

def crawl_and_copy_files_fn():
    print("Crawl and copy files")
    print("Please enter the below details")
    source_folder = massage_directory_path(input("Enter the source directory: "));
    file_ext = input("File extension to search for: ");
    file_prefix = input("File name prefix to search for: * for ALL")
    target_folder = massage_directory_path(input("Enter the target directory: "));
    copy_pref = input("Enter to O to overwrite s to skip:");
    
    for root, dirs, files in os.walk(source_folder):
        for _file in files:
            if(file_ext != "*") or (file_ext != ""):
                if _file.endswith(file_ext):
                    if(file_prefix != "*") or (file_prefix != ""):
                        if _file.startswith(file_prefix):
                            shutil.copy(os.path.abspath(root + '/' + _file), target_folder)
            else:
                if(file_prefix != "*") or (file_prefix != ""):
                        if _file.startswith(file_prefix):
                            shutil.copy(os.path.abspath(root + '/' + _file), target_folder)
                else:
                    shutil.copy(os.path.abspath(root + '/' + _file), target_folder)