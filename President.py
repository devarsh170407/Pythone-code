Age=int(input("Enter your age"))
if(Age>=35):
    if(Age>=35 and  Age<=65):
        if(Age>=35 and Age<=45):
            print("Eligible for younger president")
        else:
            print("Eligible for oldest president")
    else:
        print("NOT Eligible for president")
else:
    print("NOT Eligible for president")
