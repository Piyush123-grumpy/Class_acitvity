a=int(input("Enter the number of students in group A"))
b=int(input("Enter the number of students in group B"))
c=int(input("Enter the number of students in group C"))
if (a+b+c)%2!=0:
    number_of_benches=((a+b+c)//2)+1
    print(f"The number of benches={number_of_benches}")
else:
    number_of_benches=(a+b+c)/2
    print(f"The number of benches={number_of_benches}")