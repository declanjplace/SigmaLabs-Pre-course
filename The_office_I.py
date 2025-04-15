meet = {
    'Alice' : 2,
    'Boss' : 5, 
    'Charlie' : 9, 
    'Declan' : 1, 
    'Eve' : 4, 
    'Finley' : 8,
    'George' : 6,
    'Harold' : 7,
    'Ian' : 3,
    'Joy' : 10
}

happiness_summed = 0

for team_member in meet:
    print('{} has a happiness score of {}.\n'.format(team_member, meet[team_member]))
    happiness = meet[team_member]
    if team_member == 'Boss':
        happiness *= 2
    happiness_summed += happiness

average_happiness = happiness_summed/len(meet)

print('the average happiness of the office is {}'.format(average_happiness))

if average_happiness >= 5:
    print('Nice Work Champ!') 
else:
    print('Get Out Now!')