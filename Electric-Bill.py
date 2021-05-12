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
            "Bill": 0
            }
    
    user_tv["Model"]= input("Please insert the model of your TV: ")
    user_tv["Type"]= check_type("Please insert the type of your TV by Plasma,LED or LCD: ")
    user_tv["Size"]= Numeric_Check("Please insert the size of your TV by inches: ")
    user_tv["Hours"]= Numeric_Check("Please insert the average hours of TV used per day: ")
    user_tv["Days"]= Numeric_Check("Please insert the amount of days that you want to calculate: ")

    
    if (user_tv["Type"] == 'LED'):       
        user_tv["Bill"] = user_tv["Size"]*(1.834/1000)*39.980
    elif (user_tv["Type"] == 'LCD'):
        user_tv["Bill"] = user_tv["Size"]*(2.6/1000)*39.980
    elif (user_tv["Type"] == 'Plasma'):
        user_tv["Bill"] = user_tv ["Size"]*(5.4/1000)*39.980



    print( '\n' "Bill of your TV in drams for " ,user_tv["Hours"]," hours during ",user_tv["Days"]," days is ",user_tv["Bill"]*user_tv["Days"], " in AMD " '\n' )
    
    return user_tv

def user_data_comp():
    user_comp ={
            "Model":"",
            "Hours":0,
            "Bill":0
            }
    user_comp["Model"]= input("Please insert the model of your computer: ")
    user_comp["Hours"]= Numeric_Check("Please insert the average hours of computer used: ")
    user_comp["Wattage"]=Numeric_Check("Please insert the average Watt of your Computer: ")
    user_comp["Bill"] = user_comp["Hours"] * ((user_comp["Wattage"]/1000)*32.48) 
    user_comp["Days"]= Numeric_Check("Please insert the amount of days that you want to calculate: ")
    
    print( '\n' "Bill of your Computer in drams for " ,user_comp["Hours"]," hours is ",user_comp["Bill"], " in  AMD " '\n')
    
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

    with open('Test_data.json') as file_data:
        user_gadgets = json.load(file_data)
        return user_gadgets

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
        print('\n' "Overall bill is ", user_tv["Bill"] + user_comp["Bill"] , " AMD " '\n')

    elif(check_gadget_tv == "No" and check_gadget_comp == "No"):
        print("You have no gadgets!")
    elif(check_gadget_tv == "Yes" and check_gadget_comp == "No"):
        user_tv = user_data_tv()
        user_gadgets.append(user_tv)
    elif(check_gadget_tv == "No" and check_gadget_comp == "Yes"):
        user_comp = user_data_comp()
        user_gadgets.append(user_comp)
    else:
        print ('\n' "Please answer with only Yes or No" '\n')


    save_data(user_gadgets)


main()


