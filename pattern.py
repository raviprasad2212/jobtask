# --------------------------------------- Pattern Program1 ----------------------------------
# # Get user input data by using input method
get_data = int(input("Enter the length of the pattern"))

for count in range(1, get_data+1):
    print(count*"* ", end=" ")
    print()

# As per Testcase
# input_data = 5

# for index in range(1, input_data+1):
#     print(index*"* ", end=" ")
#     print()

# ---------------------------------------- Pattern Program2 ----------------------------------
# Get input by uisng input() method
# I have given static data
take_input = 5
for j in range(1, take_input+1):
    print("* " * j)

for i in range(take_input+1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print()

# ------------------------------------------Factorial program ---------------------------------

get_data = int(input("Enter number"))
factorial = 1

if (get_data == 0):
    print("The factorial of {} is 1".format(get_data))
if (get_data<0):
    print("The negative numbers doesnot support for factorial")
else:
    for number in range(1, get_data+1):
        factorial = factorial*number
    print("factorial of {} is".format(get_data),factorial)