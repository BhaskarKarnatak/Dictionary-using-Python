#library --------------
import json
from difflib import get_close_matches
import time
#----------------------

#accessing data from data.json file which contains dictionary words and its meaning
data = json.load(open("data.json"))

#Function used for traversing json file and finding word inside the file------------------------------------
def find(x):
    x=x.lower()
    if x in data:
        return data[x]
    elif len(get_close_matches(x,data.keys()))>0:
        yn= input("Did you mean %s instead?Enter Y if yes, or N if No : " %get_close_matches(x,data.keys())[0])
        if yn =="y" or yn =="Y":
            return data[get_close_matches(x,data.keys())[0]]
        elif yn =="N" or yn=="n":
            return "Word  not exist. Please check it again."
            
        else:
            return "**--Invalid Entry--**"
    else:
        return "Word  not exist. Please check it again."
    
#-----------------------------------------------------------------------------------------------------------


#Main Function-----------------
def main_func():
    word=input("Enter Word: ")
    output = find(word)
    if type(output) == list:
        for x in output:
            print(x)
    else:
        print(output)

    
    time.sleep(5)
    Y=input("\nWant to search more word? Enter Y if yes, or N if No : ")
    if(Y=="Y" or Y=="y"):
        print("\n")
        main_func()
    else:
        pass
#------------------------------



#calling Function 
main_func()
#----------------
