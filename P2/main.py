import EX1P2, EX2P2, EX3P2, EX4P2

option=int(input("Enter the exercise number you want to execute (1,2,3 or 4!): "))

if option==1:
    EX1P2.EX1P2()

elif option==2:
    EX2P2.EX2P2()

elif option==3:
    EX3P2.EX3P2()

elif option ==4:
    EX4P2.EX4P2()


else:
    print("Error: This is not a valid input. Only 1,2,3 or 4!)")