import os
os.system('cls') 
print("\n") 

# 1. uzdevums

# for sk in range(1 , 10000):
#     summa = 0
#     for i in range(1, sk):
#         if sk % i ==0:
#             summa += i
#     if summa == sk:
#         print(f"{sk} ir perfekts skaitlis!")

#2.uzdevums



userInput = int(input("Please enter the amount of rows: "))

row = 0
while(row < userInput):
    row += 1
    spaces = userInput - row

   

    num_stars = 2*row-1
    while(num_stars > 0):
        print("*", end='')
        num_stars -= 1

    print()
#3.uzdevums

#4.uzdevums