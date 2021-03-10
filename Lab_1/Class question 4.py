Weight=int(input("Enter the weight in to "))
unit=input("(L)bs or (K)g:")
if unit.upper() =="L":
    converted_lbs=weight*0.45
    print(f"The program wieght is {converted_lbs}killos")
elif unit.upper()=="K":
    converted_kg=weight/0.45
    print(f",The program weght is {converted_kg}pounds")
else:
    print(f'Please enter appropriate character as K for kg and L for Lbs !!')
