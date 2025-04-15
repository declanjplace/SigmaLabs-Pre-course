
name = input("Enter your name: ")
name = name.capitalize()
if name == "Alice" or name == "Bob":
    print("Hello {}!".format(name))
else:
    print("Sorry... You're not authorized to be greeted!")