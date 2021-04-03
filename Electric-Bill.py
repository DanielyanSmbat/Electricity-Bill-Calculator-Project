import json 
import os.path







def check_type(user_type):
    while(True):
        user_data = input(user_type)
        if(user_data == "Plasma" or user_data == "LED" or user_data == "LCD"):
            return user_data
        else:
            print("Please insert the type with 'Plasma' 'LED' or 'LCD'")


def user_data_tv():
    user_tv ={
            "Model":"",
            "Type":"",
            "Size": 0,
            "Hours":0,
            "Usage": 0
            }
    
    user_tv["Model"]= input("Please insert the model of your TV: ")
    user_tv["Type"]= check_type("Please insert the type of your TV by Plasma,LED or LCD: ")
    user_tv["Size"]= Numeric_Check("Please insert the size of your TV by inches: ")
    user_tv["Hours"]= Numeric_Check("Please insert the average hours of TV used per day: ")

    return user_tv


def user_data_comp():
    user_comp ={
            "Model":"",
            "Hours":0,
            "Usage":0
            }
    user_comp["Model"]= input("Please insert the model of your computer: ")
    user_comp["Hours"]= Numeric_Check("Please insert the average hours of computer used: ")
    return user_comp



def Numeric_Check(user_input):
    while(True):
        user_data = input(user_input)
        if(user_data.isnumeric()):
            user_data = float(user_data)
            return user_data
        else:
            print("Please insert a NUMBER")


def existing_gadget():
    if(os.path.exists("Test_data.json")):
        with open('Test_data.json') as file_data:
            print(file_data)
            user_gadgets = json.load(file_data)
            return user_gadgets
    else:
        return []


def save_data(user_gadgets):
    f = open("Test_data.json","w")
    f.write(json.dumps(user_gadgets,indent=2))
    f.close()



def main():

    
    print("Welcome to Electricity Bill Calculator!"'\n')
    

    user_gadgets = []
    
    user_gadgets = existing_gadget()



    
    check_gadget_tv = input("Do you have a TV please answer 'Yes' or 'No': " '\n')
    check_gadget_comp = input("Do you have a computer please answer 'Yes' or 'No': "'\n')
    if(check_gadget_tv == "Yes" and check_gadget_comp == "Yes"):
        user_tv = user_data_tv()
        user_gadgets.append(user_tv)
        print('\n' "Good Job!" '\n')
        user_comp = user_data_comp()
        user_gadgets.append(user_comp)

    elif(check_gadget_tv == "No" and check_gadget_comp == "No"):
        print("You have no gadgets!")
    elif(check_gadget_tv == "Yes" and check_gadget_comp == "No"):
        user_tv = user_data_tv()
        user_gadgets.append(user_tv)
    elif(check_gadget_tv == "No" and check_gadget_comp == "Yes"):
        user_comp = user_data_comp()
        user_gadgets.append(user_comp)
    else:
        print('\n' "Please answer with only Yes or No" '\n')
        

  

    save_data(user_gadgets)




     

main()


