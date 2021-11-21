import EX1P1, EX2P1, EX3P1, EX4P1, EX5P1

option=int(input("Enter the exercise number you want to execute (1,2,3,4 or 5): "))

if option==1:
    EX1P1.EX1P1()

elif option==2:
    EX2P1.EX2P1()

elif option==3:
    EX3P1.EX3P1()

elif option ==4:
    EX4P1.EX4P1()

elif option==5:
    EX5P1.EX5P1()

else:
    print("Error: This is not a valid input. Only 1,2,3,4 or 5!)")