
def ask_user_for_number():
    number = input('Please enter an number: ')
    if number == '':
        print('Error! No input.')    
    elif number.isdigit() == False:
        print('Error! Input is not an integer.')
    else:
        print('Your number is {}.'.format(number))
    return(int(number))

n_sum = ask_user_for_number()
m = 0
for i in range(n_sum+1):
   m += i
print("Your number summed from 1 to {} is: {}".format(n_sum,m))

n_sum_of_3s = ask_user_for_number()
m = 0
for i in range(n_sum_of_3s+1):
    v = 3*i
    if v > n_sum_of_3s:
        break
    m += v
print("The multiples of 3 from 1 to {} is: {}".format(n_sum_of_3s,m))

def product_from_1_to_n(n):
    m = 1
    for i in range(n):
        m *= i+1
    return(m)

def sum_from_1_to_n(n):
    m = 0
    for i in range(n+1):
        m += i
    return(m)

n_sum_or_product = ask_user_for_number()
print('Choose from the following: \n 1. Sum from 1 to n \n 2. Product from 1 to n')
choice = input("Choose option 1 or 2: ")
if choice == '1':
    print("Your number summed from 1 to {} is: {}.".format(n_sum_or_product, sum_from_1_to_n(n_sum_or_product)))
elif choice == '2':
    print("Your number multiplied from 1 to {} is: {}.".format(n_sum_or_product, product_from_1_to_n(n_sum_or_product)))
else:
    print('Error! Please choose either 1 or 2.')

