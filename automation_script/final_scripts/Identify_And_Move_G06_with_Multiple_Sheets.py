import os
import pandas as pd
from openpyxl import load_workbook
import shutil

f = pd.DataFrame(columns=['commodity_name', 'Not_Start "S" And 13 Char', 'A06 Folder is Empty', 'G06 Folder is Empty',
                          'move file found', 'file_name','A06_not_found','G06_not_found'])
new_path = ''
fullPath = ''


def validate_source_folder(folderName):
    if (folderName.startswith("S")):
        if (len(folderName) == 13):
            return "valid"
        else:
            return "Folder name not 13 characters"
    else:
        return "Folder name not starting with S."


def get_file_name(path):
    t = 1
    global file_full_path
    file_name = []
    FilesAndFolders = os.listdir(path)
    # print('in fn path',path)
    if FilesAndFolders:
        #         print('FilesAndFolders::',FilesAndFolders)
        for file in FilesAndFolders:  # access all things in A06 and then G06
            if (file.endswith(".xlsx")) and not (file.startswith("~$")):
                file_name.append(file)
    #                 print('file_nAMES:',file_name)
    return file_name
 
def Check_excel(chek_sheets):
    xls = pd.ExcelFile(chek_sheets, engine='openpyxl')
    sheets = xls.sheet_names
    #     print('sheets::',sheets)
    #     print('no of sheet=',len(sheets))
    if len(sheets) == 1 and sheets[0] == "Sheet1":
        return True
    else:
        return False


#     return sheets

def move_file_folder(old_path):
    global new_path
    print('old path:', old_path)
    shutil.move(old_path, new_path)


# def massage_directory_path(rawpath):
# #     print(rawpath)
#     return rawpath.replace('\\', '\\\\')

def Identify_And_Move_G06_with_Multiple_Sheets_Fn():
    global t, new_path, fullPath
    t = 1
    print("Please enter the below details")
    source_folder = (input("Enter the Input source directory: "));
    new_path = (input("Enter the Output source directory: "))
    # get all the first level folders
    allFilesAndFolders = os.listdir(source_folder)
    #     print(allFilesAndFolders)
    for i in allFilesAndFolders:
        fullPath = source_folder + "\\" + i;
        #         print('fullpath',fullPath)
        #         #Access first level folder
        if os.path.isdir(fullPath):
            # Source folder validation for S and 13 charecters
            validationOutput = validate_source_folder(i)
            if (validationOutput == "valid"):
                A06fullPath = fullPath + "\\" + "A06 TABLES"
                #                 print('A06fullpath',A06fullPath)
                if os.path.isdir(A06fullPath):
                    list_A06 = get_file_name(A06fullPath)
                    # print('list_A06', list_A06)  # all files in A06 table
                    if list_A06:
                        for files in list_A06:
                            file_full_path = A06fullPath + "\\" + files
                            Standard = Check_excel(file_full_path)
                            if not Standard:
                                # print('false file:', file_full_path)
                                f.loc[t, 'commodity_name'] = i
                                f.loc[t, 'file_name'] = files
                                t += 1
                                move_file_folder(fullPath)
                                break
                        if Standard:
                            G06fullPath = fullPath + "\\" + "G06 TABLES"
                            if os.path.isdir(G06fullPath):
                                list_G06 = get_file_name(G06fullPath)
                                if list_G06:
                                    #                             print('list_G06',list_G06)
                                    for files in list_G06:
                                        file_full_path = G06fullPath + "\\" + files
                                        Standard = Check_excel(file_full_path)
                                        if not Standard:
                                            # print('false file:', file_full_path)
                                            f.loc[t, 'commodity_name'] = i
                                            f.loc[t, 'file_name'] = files
                                            t += 1
                                            move_file_folder(fullPath)
                                            break
                                else:
                                    #                             print("G06 folder empty")
                                    f.loc[t, 'commodity_name'] = i
                                    f.loc[t, 'G06 Folder is Empty'] = "✓"
                                    t += 1
                                    move_file_folder(fullPath)
                            else:
                                print("G06 table folder not found")
                                f.loc[t, 'commodity_name'] = i
                                f.loc[t, 'G06_not_found'] = "✓"
                                t += 1
                                move_file_folder(fullPath)
                                    
                    else:
                        #                     print("A06 folder is empty")
                        f.loc[t, 'commodity_name'] = i
                        f.loc[t, 'A06 Folder is Empty'] = "✓"
                        t += 1
                        move_file_folder(fullPath)
                        
                else:
                    print("A06 Table folder not found")
                    f.loc[t, 'commodity_name'] = i
                    f.loc[t, 'A06_not_found'] = "✓"
                    t += 1
                    move_file_folder(fullPath)
                    
            else:
                #                 print("not start with 13 chr and S")
                f.loc[t, 'commodity_name'] = i
                f.loc[t, 'Not_Start "S" And 13 Char'] = "✓"
                t += 1
                move_file_folder(fullPath)

        else:
            print(fullPath)
            Standard = Check_excel(fullPath)
            #             print('standard::',Standard)
            if not Standard:
                f.loc[t, 'commodity_name'] = i
                f.loc[t, 'move file found'] = "✓"
                t += 1
                move_file_folder(fullPath)
    f.to_excel('Identify_And_Move_G06_with_Multiple_Sheets.xlsx', index=False)
