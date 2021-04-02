import json 
import os.path


def user_data_tv():
    user_tv ={
            "Model":"",
            "Type":"",
            "Size":0,
            "Hours":0
            }
    user_tv["Model"]= input("Please insert the model of your TV: ")
    user_tv["Type"]= input("Please insert the type of your TV by Plasma,LED or LCD: ")
    user_tv["Size"]= Numeric_Check("Please insert the size of your TV by inches: ")
    user_tv["Hours"]= Numeric_Check("Please insert the average hours of TV used: ")
    return user_tv


def user_data_comp():
    user_comp ={
            "Model":"",
            "Hours":0
            }
    user_comp["Model"]= input("Please insert the model of your computer: ")
    user_comp["Hours"]= Numeric_Check("Please insert the average hours of computer used: ")
    return user_comp


def Numeric_Check(user_input):
    while(True):
        user_data = input(user_input)
        if(user_data.isnumeric()):
            user_data = int(user_data)
            return user_data
        else:
            print("Please insert a NUMBER")



def main():
    
    print("Welcome to Electric Bill Calculator!Please fill the data for your gadgets and if you don't have that precise gadget type '0' ")
    
    user_data_tv()
    
    user_data_comp()
    
    Numeric_Check()
    

main()


