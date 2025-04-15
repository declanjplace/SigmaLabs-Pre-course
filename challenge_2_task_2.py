import random

def options_menu():
    # Function which makes a menu for the user to choose what type of username they want
    print("Welcome to the username creator. Please choose one of the following options")
    print("1. Create username based on a name")
    print("2. Generate a random username")


def reverse_name(name):
    # Function which reverses the order of a string
    print(name[::-1])
    return(name[::-1])


def intersperse_name(name, surname):
    # Function which takes a first and last name,
    # reverses the first name
    # then intersperses the reversed first name and last name every other digit
    interspersed_name = reverse_name(name)
    n = 0
    m = 0
    for i in surname:
        interspersed_name = interspersed_name[:m+1] + surname[n] + interspersed_name[m+1:]
        n += 1
        m += 2
    print(interspersed_name)
    return(interspersed_name)

def format_name(name):
    # Function which splits a string in half to create a capitalized full name
    half_of_name_length = int(0.5 * len(name))
    new_full_name = name[:half_of_name_length].capitalize() + ' ' + name[half_of_name_length:].capitalize()
    print(new_full_name)
    return(new_full_name)

random_variables = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

def random_username_generator():
    # Function which creates a randomly generated full name
    username = ""
    for i in range(10):
        variable = random.choice(random_variables)
        username = username + variable
    final_username = username[:5].capitalize() + ' ' + username[5:].capitalize()
    return(final_username)


user_name = ""
def main():
    # Function which runs the application to make a username
    while True:
        options_menu()
        choice = input("Choose option 1 or 2: ")
        if choice == "1":
            forename = input('Enter your first name: ')
            surname = input('Enter your surname: ')
            interspersed_name = intersperse_name(forename, surname)
            user_name = format_name(interspersed_name)
            print("Your knew username is: {}".format(user_name))
        elif choice == "2":
            user_name = random_username_generator()
            print("Your knew username is: {}".format(user_name))
        else:
            print('Error! Please choose either 1 or 2.')

main()
