import os
import pandas as pd
import logging
from pathlib import Path
import openpyxl

df1 = pd.DataFrame(
    columns=['Orignal_file_Name', '"A"And13Chr', 'G06_NF_in_File_name', 'Rename_File_Name', 'Extra_G06_in_File_name'])

def validate_source_file(fileName):
    if (fileName.startswith("A")):
        if (len(fileName) > 18):
            #             print('fileName:::::::::',fileName)
            return "valid"
        else:
            return "fileName not 13 characters"
    else:
        return "fileName not starting with A."


def Part_Renaming_Fn():
    t = 1
    logging.basicConfig(filename='Untitled.log', encoding='utf-8', level=logging.DEBUG)
    logging.info('Part_Renaming_Fn function loaded: ')
    #     print("Part_Renaming_Fn")
    #     print("Please enter the below details")
    source_folder = (input("Enter the xlsx source directory: "))
    allFilesAndFolders = os.listdir(source_folder)
    for i in allFilesAndFolders:
        rename = False
        fullpath = source_folder + '\\' + i
        #         print('xlsx file name::',i)
        if os.path.exists(fullpath):
            validation = validate_source_file(i)
            if (validation == "valid"):
                #                 print("match vaild")
                print('fullpath:;', fullpath)
                workbook = openpyxl.load_workbook(fullpath)
                worksheet = workbook.active
                column = 'M'
                max_rows = worksheet.max_row
                unique_data = set()
                for row in range(2, max_rows + 1):
                    cell_value = worksheet[f'{column}{row}'].value
                    if cell_value is not None:
                        cell_value = cell_value.split('&')
                        #                         print('cell_value',cell_value)
                        [unique_data.add(item.strip()) for item in cell_value]
                #
                #                 print('unique_data:::::',unique_data)
                data = list(unique_data)
                print('final_data:::::', data)
                result = ''
                for n in range(len(data)):
                    result += data[n]
                    if n != len(data) - 1:
                        result += '_'
                #                 print(result)
                rename_name = i[:13] + "_" + result + ".xlsx"
                print('rename_name:::', rename_name)
                print('xlsx file name::', i)
                rename_path = os.path.join(source_folder, rename_name)
                for GO6_code in data:
                    if GO6_code in i:
                        print("found", GO6_code)

                    else:
                        print('G06_code_not Found..!!')
                        df1.loc[t, 'Orignal_file_Name'] = i
                        df1.loc[t, 'G06_NF_in_File_name'] = GO6_code
                        print('need to rename the file..!!')
                        #os.rename(fullpath, rename_path)
                        df1.loc[t, 'Orignal_file_Name'] = i
                        # df1.loc[t, 'Rename_File_Name'] = rename_name
                        print('need to rename the file..!!')
                        print("file rename successfully....!!")
                        rename = True
                        break
                d = (i.split(".")[0]).split('_')
                d = [s.replace(' ', '').strip() for s in d if s.strip()]
                for code in d:
                    if code not in rename_name:
                        print('code not found in file::', code)
                        df1.loc[t, 'Orignal_file_Name'] = i
                        df1.loc[t, 'Extra_G06_in_File_name'] = code
                        rename = False
                if rename:
                    os.rename(fullpath, rename_path)
                    df1.loc[t, 'Orignal_file_Name'] = i
                    df1.loc[t, 'Rename_File_Name'] = rename_name

            else:
                print('Validation fail..!!')
                df1.loc[t, 'Orignal_file_Name'] = i
                df1.loc[t, '"A"And13Chr'] = "✓"
            t += 1

    df1.to_excel('Part_Renaming_FN.xlsx', index=False)
    print("Part_Renaming_FN CONVERSION DONE.....!!")
# Part_Renaming_Fn()
