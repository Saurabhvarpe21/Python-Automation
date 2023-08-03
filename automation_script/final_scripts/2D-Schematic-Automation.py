from steps.Identify_And_Move_G06_with_Multiple_Sheets import Identify_And_Move_G06_with_Multiple_Sheets_Fn
# from steps.crawl_and_copy_files import crawl_and_copy_files_fn
from steps.RT_File_rename import RT_File_rename_fn
from steps.RT_NA_to_CUSTOM_IMAGE import RT_NA_to_CUSTOM_IMAGE_fn
from steps.IT_JPG_TO_PNG import IT_JPG_TO_PNG_FN
# from steps.Copy_and_Move_Snipped_Images import Copy_and_Move_Snipped_Images_FN
from steps.COPY_AND_MOVE_CIRCUIT_SNIPPED_IMAGES import COPY_AND_MOVE_SNIPPED_IMAGES_FN
from steps.DB_SHEET_UPDATE import DB_SHEET_UPDATE_FN
from steps.Part_Renaming import Part_Renaming_Fn
import logging

def crawl_and_copy_folders():
    print("WIP 1")

def intro_msg():
    logging.basicConfig(filename='2D-Schematic-Automation.log', encoding='utf-8', level=logging.DEBUG)
    logging.info('2D-Schematic-Automation script loaded') 
    print("Welcome to Automation Master Script.")
    print("Please enter what you want to do ?")
    print("..................................")
    print("Pick one of the below steps to execute,")
    print("1: RT_File_rename")
    print("2: Identify_And_Move_G06_with_Multiple_Sheets")
    print("3: RT_NA_to_CUSTOM_IMAGE_fn")
    print("4: IT_JPG_TO_PNG")
    print("5: COPY_AND_MOVE_CIRCUIT_SNIPPED_IMAGES")
    print("6: DB_SHEET_UPDATE")
    print("7: Part_Renaming")
    return input()
    
def main():
    step = intro_msg()
    print(step)
    if(step == "1"):
        RT_File_rename_fn()
    elif(step == "2"):
        Identify_And_Move_G06_with_Multiple_Sheets_Fn()
    elif(step == "3"):
        RT_NA_to_CUSTOM_IMAGE_fn()
    elif(step == "4"):
        IT_JPG_TO_PNG_FN()
    elif(step == "5"):
        COPY_AND_MOVE_SNIPPED_IMAGES_FN()
    elif(step == "6"):
        DB_SHEET_UPDATE_FN()
    elif(step == "7"):
        Part_Renaming_Fn()
    else:
        print("enter the step")
        
main()