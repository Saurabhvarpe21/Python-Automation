from add import addition
from sub import subtraction
from mul import multiplication
from div import division
from excel import excel_to_html

def operations(**input):


    if input[0]["value"] == "1":
        return addition(input[0]["a"],input[0]["b"])
    elif input[0]["value"] == "2":
        return subtraction(input[0]["a"],input[0]["b"])
    elif input[0]["value"] == "3":
        return multiplication(input[0]["a"],input[0]["b"])
    elif input[0]["value"] == "4":
        return division(input[0]["a"],input[0]["b"])
    elif input[0]["value"] == "5":
        return excel_to_html(input[0]["inputpath"])


