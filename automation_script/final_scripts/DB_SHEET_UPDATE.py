import os
import pandas as pd
import logging
import openpyxl
from openpyxl import load_workbook

DB_DF = pd.DataFrame(
    columns=['commodity_name', 'Not_Start "S" And 13 Char', 'DB-SHEET_NOT_FOUND', 'Cont_Desc_not_found'])


def validate_source_folder(folderName):
    if (folderName.startswith("S")):
        if (len(folderName) == 13):
            return "valid"
        else:
            return "Folder name not 13 characters"
    else:
        return "Folder name not starting with S."


def DB_SHEET_UPDATE_FN():
    t = 1
    logging.basicConfig(filename='Untitled.log', encoding='utf-8', level=logging.DEBUG)
    logging.info('DB_SHEET_UPDATE function loaded: ')
    print("DB_SHEET_UPDATE")
    print("Please enter the below details")
    source_folder = (input("Enter the COMMODITY source directory: "))
    DataBaseSheet_master = (input("Enter the DataBaseSheet_MasterData directory: "))
    allFilesAndFolders = os.listdir(source_folder)
    for i in allFilesAndFolders:
        fullpath = source_folder + '\\' + i
        print(fullpath)
        if os.path.isdir(fullpath):
            validation = validate_source_folder(i)
            if (validation == "valid"):
                DB_SHEET_path = fullpath + '\\' + i + "_DB.xlsx"
                if os.path.exists(DB_SHEET_path):
                    print("DB_SHEET_path****::", DB_SHEET_path)
                    # df =pd.DataFrame()
                    df = pd.read_excel(DB_SHEET_path)
                    wb = load_workbook(DB_SHEET_path)
                    ws = wb._sheets[0]
                    cl = df.columns
                    le = df.shape[0]
                    writer = pd.ExcelWriter(DB_SHEET_path, engine='xlsxwriter')
                    df.to_excel(writer, sheet_name='Sheet1', index=False)
                    workbook = writer.book
                    worksheet = writer.sheets['Sheet1']
                    header_format = workbook.add_format({'bottom': 2, 'bg_color': '#FFFF00', 'border': 1})
                    header_format.set_align('center')
                    header_format.set_align('vcenter')
                    for col_num, value in enumerate(df.columns.values):
                        worksheet.write(0, col_num, value, header_format)
                    writer.save()
                    # writer.close()
                    print('yellow header is added###########')
                    for r in range(0, le):
                        if str(df[cl[1]][r]) == 'nan' and str(df[cl[2]][r]) == 'nan' and str(df[cl[3]][r]) == 'nan':
                            Connector_Description = str(df[cl[0]][r])
                            print('Connector_Description::""""""', Connector_Description)
                            DB_MASTER = pd.read_excel(DataBaseSheet_master)
                            name_to_search = Connector_Description
                            result = DB_MASTER[DB_MASTER.iloc[:, 0] == name_to_search]
                            if result.empty:
                                print(f"{name_to_search} not found in the first column of the Excel sheet.")
                                DB_DF.loc[t, 'commodity_name'] = i
                                DB_DF.loc[t, 'Cont_Desc_not_found'] = Connector_Description
                                t += 1
                            else:
                                print(f"{name_to_search} found in the following rows:")
                                df.at[r, cl[1]] = (result['Connector Numbers'].to_list())[0]
                                df.at[r, cl[2]] = (result['No of Cavities'].to_list())[0]
                                df.at[r, cl[3]] = (result['CONNECTOR TYPE'].to_list())[0]
                                df.at[r, cl[7]] = (result['Connector Color'].to_list())[0]
                                df.to_excel(DB_SHEET_path, index=False)
                                print('done')
                else:
                    print('DB_sheet not found')
                    DB_DF.loc[t, 'commodity_name'] = i
                    DB_DF.loc[t, 'DB-SHEET_NOT_FOUND'] = i + "_DB.xlsx"

            else:
                print('validation fail')
                DB_DF.loc[t, 'commodity_name'] = i
                DB_DF.loc[t, 'Not_Start "S" And 13 Char'] = "✓"
            t += 1

        else:
            os.remove(fullpath)  # other file deleted only folders are there
            print('file deleteed::', i)

    DB_DF.to_excel('DB_SHEET_UPDATE.xlsx', index=False)
    print("DB_SHEET_UPDATE CONVERSION DONE.....!!")

