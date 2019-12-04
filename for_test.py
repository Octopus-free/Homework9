from random import sample


sack = []

for sack_number in range(0, 91):
    sack.append(sack_number)

print(sack)

card_row = []

border_counter = 1
for counter in range(1, 9):
    border_counter += 1
    choice = sample(sack[int('{0}{1}'.format(counter, '0')):int('{0}{1}'.format(border_counter, '0'))], 1)[0]
    while choice == ' ':
        choice = sample(sack[int('{0}{1}'.format(counter, '0')):int('{0}{1}'.format(border_counter, '0'))], 1)[0]
    card_row.append(choice)
    sack[choice] = ' '

print(card_row)
print(sack)
print(sample(card_row, 1)[0])