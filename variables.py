
number = []
for i in range(0,5):
    input_number= int(input("enter number: "))
    number.append(input_number)
    print(number)


# # I am trying to accept the four numbers
# number_one = int(input("Insert your age "))
# number_two = int(input("Insert your heigt "))
# number_three = int(input("Insert your weight "))
# number_four = int(input("Insert your family members "))

choice = input("enter your prefered calculation: average, multiply or sum  ")

# calculate the average
average = (number[0] + number[1] + number[2] + number[3] + number[4])/5

# calculate the sum
sum = number[0] + number[1] + number[2] + number[3] + number[4]

# calculate the multiplication
multiply =number[0] + number[1] + number[2] + number[3] + number[4]

# display the result based on the condition/ chioce
if(choice == "average"):
     print("the avrage of the numbers is: ", average)
elif(choice == "sum"):
    print("the sum of the numbers: ", sum)
elif(choice == "multiply"):
     print("the multiplication of the numbers: ", multiply)
else:
     print(average, sum, multiply)
     