import os
import pandas as pd
import logging

df = pd.DataFrame(columns=['commodity_name',
                           'Not_Start "S" And 13 Char',
                           'A06_not_found', 'G06_not_found',
                           'A06 Folder is Empty',
                           'G06 Folder is Empty',
                           'SNIP_IMG_fol_not_found',
                           'SNIPPED_IMAGES_fold_Empty'])


def validate_source_folder(folderName):
    if (folderName.startswith("S")):
        if (len(folderName) == 13):
            return "valid"
        else:
            return "Folder name not 13 characters"
    else:
        return "Folder name not starting with S."


def IT_JPG_TO_PNG_FN():
    t = 1
    logging.basicConfig(filename='Untitled.log', encoding='utf-8', level=logging.DEBUG)
    logging.info('IT_JPG_TO_PNG_FN function loaded: ')
    print("IT_JPG_TO_PNG_FN")
    print("Please enter the below details")
    source_folder = (input("Enter the source directory: "))
    allFilesAndFolders = os.listdir(source_folder)
    for i in allFilesAndFolders:
        fullpath = source_folder + '\\' + i
        print('fullpath:', fullpath)
        if os.path.isdir(fullpath):
            validation = validate_source_folder(i)
            if (validation == "valid"):
                A06_Full_path = fullpath + "\\" + "A06 TABLES"
                #                A06_Full_path=os.path.join(fullpath,"A06 TABLES") another way
                if os.path.isdir(A06_Full_path):
                    A06fileandfolder = os.listdir(A06_Full_path)
                    if A06fileandfolder:
                        print('A06 not empty')
                    else:
                        print('A06 folder is empty')
                        df.loc[t, 'commodity_name'] = i
                        df.loc[t, 'A06 Folder is Empty'] = "✓"

                else:
                    print('A06 folder not found')
                    df.loc[t, 'commodity_name'] = i
                    df.loc[t, 'A06_not_found'] = "✓"
                G06_Full_path = fullpath + "\\" + "G06 TABLES"
                if os.path.isdir(G06_Full_path):
                    G06fileandfolder = os.listdir(G06_Full_path)
                    if G06fileandfolder:
                        print('G06 not empty')
                    else:
                        print('G06 folder is empty')
                        df.loc[t, 'commodity_name'] = i
                        df.loc[t, 'G06 Folder is Empty'] = "✓"

                else:
                    print('G06 folder not found')
                    df.loc[t, 'commodity_name'] = i
                    df.loc[t, 'G06_not_found'] = "✓"

                SNIPPED_IMAGES = fullpath + "\\" + "SNIPPED IMAGES"
                if os.path.isdir(SNIPPED_IMAGES):
                    ALL_SNIPPED_IMAGESS = os.listdir(SNIPPED_IMAGES)
                    #                     print("ALL_SNIPPED_IMAGESS:",ALL_SNIPPED_IMAGESS)
                    if ALL_SNIPPED_IMAGESS:
                        hiddan_file = [i for i in ALL_SNIPPED_IMAGESS if i.endswith(".db")]
                        print("hiddan_file:", hiddan_file)
                        dup_file = []
                        images = []
                        for file in ALL_SNIPPED_IMAGESS:
                            if file.split('.')[0] in images:
                                dup_file.append(file)

                            else:
                                images.append(file.split('.')[0])
                        print('dup_file::', dup_file)
                        #                         print('images::',images)
                        for file in dup_file + hiddan_file:
                            os.remove(SNIPPED_IMAGES + "\\" + file)

                        ALL_SNIPPED_IMAGESS1 = os.listdir(SNIPPED_IMAGES)
                        #                         print("updates_ALL_SNIPPED_IMAGES1::",ALL_SNIPPED_IMAGESS1)
                        for p in ALL_SNIPPED_IMAGESS1:
                            path_ = SNIPPED_IMAGES + "\\" + p
                            if p.endswith(".jpg"):
                                os.rename(path_, path_[:-3] + "png")

                    else:
                        print('SNIPPED_IMAGES folder is empty')
                        df.loc[t, 'commodity_name'] = i
                        df.loc[t, 'SNIPPED_IMAGES_fold_Empty'] = "✓"


                else:
                    print('SNIPPED_IMAGES folder not found')
                    df.loc[t, 'commodity_name'] = i
                    df.loc[t, 'SNIP_IMG_fol_not_found'] = "✓"

            else:
                print('validation fail')
                df.loc[t, 'commodity_name'] = i
                df.loc[t, 'Not_Start "S" And 13 Char'] = "✓"
            t += 1

        else:
            os.remove(fullpath)
            print('file deleteed::', i)

    df.to_excel('IT_JPG_TO_PNG.xlsx', index=False)
    print("IT_JPG_TO_PNG CONVERSION DONE.....!!")
