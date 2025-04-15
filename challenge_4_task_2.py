animals = [
    {'name' : 'Fluffy', 'type' : 'dog'},
    {'name' : 'Parsley', 'type' : 'dog'},
    {'name' : 'Ginger', 'type' : 'cat'},
    {'name' : 'Biscuit', 'type' : 'cat'}
]

def say_hello_to_pet(pets):
    for pet in pets:
        hello_message = ''
        if pet['type'] == 'dog':
            hello_message = 'Woof'
            pet_name = pet['name']
        elif pet['type'] == 'cat':
            hello_message = 'Meow'
            pet_name = pet['name']
        print(f'{hello_message}, {pet_name}!')
# fyi: I made Task 3: Raising Exception a in separate file 
# called challenge_4_task_3, thanks.

if __name__ == '__main__':
    say_hello_to_pet(animals)

