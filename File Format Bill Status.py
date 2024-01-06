l1=["C", "C++", "Java", "Python", ".Net", "ASP.net"]
course=input("Enter Course Name: ")
if(course in l1):
    name=input("Enter Your Name: ")
    fees=int(input("Enter the fees: "))
    f1=open("Bill1.txt", "w")
    f1.write("***Welcome to Gops IT Technologies***\n")
    f1.write(f"Name is : {name}\n")
    f1.write(f"Course Name is : {course}\n")
    f1.write(f"Fees is : {fees}\n")
    f1.write("Thank You!")
    print("Bill was Created")
    print("Read the student details")
    f1=open("Bill1.txt", "r")
    print(f1.read())
    f1.close()
else:
    print("Your Selecting Course is Not available...!")

