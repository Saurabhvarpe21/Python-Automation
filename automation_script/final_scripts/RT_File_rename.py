#from utils.stringUtils import massage_directory_path
import logging
import os
import pandas as pd
df=pd.DataFrame(columns=['commodity_name','Not_Start "S" And 13 Char','G06 Folder is Empty','File Not Rename'])


def validate_source_folder(folderName):
    if(folderName.startswith("S")):
        if(len(folderName)==13):
            return "valid"
        else:
            return "Folder name not 13 characters"
    else:
        return "Folder name not starting with S."


def massage_directory_path(rawpath):
    print(rawpath)
    return rawpath.replace('\\', '\\\\')

def slice_for_A13(string):
    #find the index of A in the string 
    Apos = string.find('A');
    if(Apos == -1):
        return "INVALID"
    else:
        subStr = string[Apos:Apos+13];
        if "." in subStr:
            return "INVALID"
        else:
            #replace _ with -
            return subStr.replace("_","-");
            
        
def RT_File_rename_fn():
    t=1
    logging.basicConfig(filename='Untitled.log', encoding='utf-8', level=logging.DEBUG)
    logging.info('RT_File_rename_fn function loaded: ') 
    print("RT_File_rename")
    print("Please enter the below details")
    source_folder = massage_directory_path(input("Enter the source directory: "));
    # get all the first level folders
    allFilesAndFolders =os.listdir(source_folder)
    
    for i in allFilesAndFolders:
        fullPath = source_folder + "\\" + i;
        #Access first level folder
        if os.path.isdir(fullPath):
            #Source folder validation for S and 13 charecters
            validationOutput = validate_source_folder(i)
            if(validationOutput == "valid"):
                g06fullPath = fullPath + "\\" + "G06 TABLES"
                #Check for G06 TABLES
                if os.path.isdir(g06fullPath):
                    allG06FilesAndFolders =os.listdir(g06fullPath)
                    print(allG06FilesAndFolders)
                    if not allG06FilesAndFolders:
                        df.loc[t,'commodity_name']=i
                        df.loc[t,'G06 Folder is Empty']="✓"
                        t+=1
                        
                    for j in allG06FilesAndFolders:
                        fp = g06fullPath + "\\" 
                        currentObj = fp + j;
                        if(os.path.isfile(currentObj)):
                            #Form new file name
                            oldFileFullPath = fp+j;
#                             print("oldFileFullPath: ",oldFileFullPath );
                            if(j.endswith(".xlsx")):
                                log = slice_for_A13(j)
                                str2 = log;str1 = i;
                                newFileName= str1 + "_G06_" + str2 + ".xlsx";
                                newFileFullPath = fp+newFileName;
#                                 print("newFileFullPath: ",newFileFullPath );
                                if(log == "INVALID"):
                                    
                                    df.loc[t,'commodity_name']=i
                                    df.loc[t,'File Not Rename']=j
                                    t+=1
        
#                                     print("INVALID file name: ", oldFileFullPath)
                                else:
                                    print('oldFileFullPath',oldFileFullPath)
                                    print('newFileFullPath',newFileFullPath)
                                    os.rename(oldFileFullPath, newFileFullPath)
                                    
                            else:
                                os.remove(oldFileFullPath)                        
                else:
                    print("G06 TABLES folder not found")
            else:
                df.loc[t,'commodity_name']=i
                df.loc[t,'Not_Start "S" And 13 Char']="✓"
                t+=1
#                 print(i + " : " + validationOutput)
            
    df.to_excel('RT_FILE_RENAME.xlsx',index=False)