departments = {
    'accounts' : 1,
    'finance' : 2,
    'canteen' : 10,
    'regulation' : 3,
    'trading' : 6,
    'change' : 6,
    'IS' : 8,
    'retail' : 5,
    'cleaning' : 4,
    'pissing about' : 25,
}

staff = {
    'Alice' : 'finance',
    'Boss' : 'regulation', 
    'Charlie' : 'IS', 
    'Declan' : 'retail', 
    'Eve' : 'accounts', 
    'Finley' : 'IS',
    'George' : 'canteen',
    'Harold' : 'accounts',
    'Ian' : 'cleaning',
    'Joy' : 'pissing about'
}

cumulative_score = 0

for worker in staff:
    if (staff[worker] in departments) == True:
        cumulative_score += departments[staff[worker]]
    else:
        print('{} is not in a valid department!'.format(worker.capitalize()))

print(cumulative_score)

if cumulative_score <= 80:
    print('kill me now')
elif cumulative_score < 100:
    print('i can handle this')
elif cumulative_score >= 100:
    print('party time!!')
else:
    print('Error')