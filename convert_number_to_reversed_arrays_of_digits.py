def digitize(n):
    digits_array = []
    number_string = str(n)
    reversed_number_string = number_string[::-1]
    for i in range(len(reversed_number_string)):
        n = int(reversed_number_string[i])
        digits_array.append(n)
    
    return(digits_array)

print(digitize(12345))