import os
import pandas as pd
import logging
from openpyxl import load_workbook
import shutil
from pathlib import Path
df1= pd.DataFrame(columns=['commodity_name', 'Not_Start "S" And 13 Char','G06_OR_SNIP_FOL_NF','G06 Folder is Empty'
                          ,'Repo_sub_fol_NF','SNIP_IMG_NF'])

def validate_source_folder(folderName):
    if(folderName.startswith("S")):
        if(len(folderName)==13):
            return "valid"
        else:
            return "Folder name not 13 characters"
    else:
        return "Folder name not starting with S."
    
def COPY_AND_MOVE_SNIPPED_IMAGES_FN():
    t=1
    logging.basicConfig(filename='Untitled.log', encoding='utf-8', level=logging.DEBUG)
    logging.info('COPY_AND_MOVE_SNIPPED_IMAGES_FN function loaded: ') 
    print("COPY_AND_MOVE_SNIPPED_IMAGES_FN")
    print("Please enter the below details")
    source_folder =(input("Enter the COMMODITY source directory: "))
    Sni_Img_Rep = (input("Enter the Snipped Image Repository source directory: "))
    allFilesAndFolders=os.listdir(source_folder)
    snip_repo_folder=os.listdir(Sni_Img_Rep)
    for i in allFilesAndFolders:
        fullpath=source_folder + '\\' + i
        if os.path.isdir(fullpath):
            validation=validate_source_folder(i)
            if (validation=="valid"):
                G06_Full_path= fullpath + "\\" + "G06 TABLES"
                SNIPPED_IMAGES_path= fullpath + "\\" + "SNIPPED IMAGES"
                if os.path.isdir(G06_Full_path) and os.path.isdir(SNIPPED_IMAGES_path):
                    
                    comm_snip_image=os.listdir(SNIPPED_IMAGES_path)
                    comm_snip_image=[i for i in comm_snip_image if not i.endswith(".db")]
                    comm_snip_image = [Path(i).stem for i in comm_snip_image]
                    print('comm_snip_image::',comm_snip_image)
                    print('G06_Full_path::',G06_Full_path)
                    G06fileandfolder=os.listdir(G06_Full_path)
                    if G06fileandfolder:
                        print('G06 not empty') 
                        for m in G06fileandfolder:
                            print('m::',m)
                            xl_path=G06_Full_path+"\\"+ m
                            df=pd.read_excel(xl_path)
                            wb = load_workbook(xl_path)
                            ws = wb._sheets[0]
                            cl = df.columns
                            le = df.shape[0]
                            dev_list=[]
                            G06_part_no_list=[]
                            for r in range (0,le):
                                if str(df[cl[10]][r]) == 'nan' and str(df[cl[11]][r])!= 'nan' and str(df[cl[12]][r])!= 'nan':
                                    if str(df[cl[11]][r]) not in dev_list and  str(df[cl[11]][r]) not in comm_snip_image:   
                                        dev_list.append(str(df[cl[11]][r]))
                                        G06_part_no_list.append(str(df[cl[12]][r]))
                            print("dev_list::",dev_list)
                            print("G06_part_no_list::",G06_part_no_list)
                            for dev in range(len(dev_list)):
                                print("dev_list::",dev_list[dev])
                                print("G06_part_no_list::",G06_part_no_list[dev])
                                repo_path=(Sni_Img_Rep +"\\"+ G06_part_no_list[dev])
                                img_path=(repo_path +'\\'+ dev_list[dev])
                                ext = ['.jpg', '.JPG', '.PNG', '.png']
                                img_found=False
                                for ex in ext:
                                    if (os.path.isdir(repo_path)):
                                        if os.path.exists(img_path+ex):
                                            img_found=True
                                            print('img_path_in_repo:::::::',img_path+ex)
                                            shutil.copy(img_path+ex,SNIPPED_IMAGES_path)
                                    else:
                                        print('Sni_Img_Rep_SUB_folder not found::',repo_path)
                                        df1.loc[t,'commodity_name']=i
                                        df1.loc[t,'Repo_sub_fol_NF']=G06_part_no_list[dev]
                                       
#                                         break
                                        
                                if not img_found:
                                    print('SNIP_image is not found::',img_path)
                                    df1.loc[t,'commodity_name']=i
                                    df1.loc[t,'SNIP_IMG_NF']=dev_list[dev]
                                    
                    else:
                        print('G06 folder is empty')
                        df1.loc[t,'commodity_name']=i
                        df1.loc[t,'G06 Folder is Empty']="✓"
                        
                else:
                    print('G06 folder  or snipped image folder not found')
                    df1.loc[t,'commodity_name']=i
                    df1.loc[t,'G06_OR_SNIP_FOL_NF']="✓"
                                       
            else:
                print('validation fail')
                df1.loc[t,'commodity_name']=i
                df1.loc[t,'Not_Start "S" And 13 Char']="✓"
            t+=1  
        
        else:
            os.remove(fullpath)
            print('file deleteed::',i)
 
    df1.to_excel('COPY_AND_MOVE_SNIPPED_IMAGES_FN.xlsx',index=False)
    print("COPY_AND_MOVE_SNIPPED_IMAGES_FN CONVERSION DONE.....!!")    
# COPY_AND_MOVE_SNIPPED_IMAGES_FN()
