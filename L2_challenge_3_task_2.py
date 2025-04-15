

Jane_Doe = {
    'Name' : 'Jane Doe',
    'Age' : 42,
    'Employed?' : 'Yes'
}

Tom_Smith = {
    'Name' : 'Tom Smith', 
    'Age' : 18,
'Employed?' : 'Yes'
}

Mariam_Coulter = {
    'Name' : 'Mariam Coulter', 
    'Age' : 66,
    'Employed?' : 'No'
}

Gregory_Tims = {
    'Name' : 'Gregory Tims',
    'Age' : 8,
    'Employed?' : 'No'
}

people = [Jane_Doe, Tom_Smith, Mariam_Coulter, Gregory_Tims]

def print_data_in_list():
    for person in people:
        print('Name: {}\nAge: {}\nEmployed: {}\n'.format(person['Name'], person['Age'], person['Employed?']))

print_data_in_list()
while True:
    prompt = input('Would you like to Add or Remove data from the dictionary? ')
    if prompt == 'Add':
        new_first_name = input('Please enter the persons first name: ')
        new_last_name = input('Please enter the persons last name: ')
        new_full_name = new_first_name + ' ' + new_last_name
        new_age = int(input('Please enter the persons age: '))
        new_employed = input('Please enter the persons employment status, Yes or No: ')
        new_person = {
            'Name' : new_full_name,
            'Age' : new_age,
            'Employed?' : new_employed
        }
        people.append(new_person)
        print_data_in_list()
    elif prompt == 'Remove':
        remove = input('Who would you like to remove? ')
        for person in people:
            if remove == person['Name']:
                people.pop(person)
            else:
                remove = input('Data not found. Please try again: ')
                continue
        print_data_in_list()
    else:
        print('Invalid input! Please input either "Add" or "Remove": ')
        continue
            


