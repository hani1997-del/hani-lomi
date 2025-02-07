# # # array deccliration
hotels = []  
# hotels.append("Sheraton")
# print(hotels)

# for i in range(0,5):
#     hotel_input = input('enter the hotel name:' )
#     hotels.append(hotel_input)

# print(hotels)

user_input = input('enter vaalues separated by by commas: ')

# splitting the input into a list
input_values = user_input.split(',')

#initialize an empty list
result_array =[]

# loop through the input values and append to the array
for value in input_values:
    # stripe anywhitespace and append to the result array
    result_array.append(value.strip())

# output the result array
print("resulting array:", result_array)