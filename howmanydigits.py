no=int(input("Enter Any Number"))
if no>=1 and no<=9:
    print("1 digit number")
else:
    if (no>=10 and no<=99):
        print("2 digit number")
    else:
        if no>=100 and no<+999:
            print("3 digit number") 
        else:
            print("more than 3")       