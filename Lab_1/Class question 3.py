Name=input("Enter the name:")
length=len(Name)
if length<3:
    print(f'The name is weird')
elif length>50:
    print(f'The name is ugly')
else :
    print(f'The name is good')