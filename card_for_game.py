from random import sample


def under_line(func):
    def inner():
        print('--'*13)
        result = func()
        return result
    return inner


@under_line
def row_generator():
    sack = []
    card_row = []

    for sack_number in range(0, 91):
        sack.append(sack_number)
    border_counter = 1

    choice = sample(sack[0:10], 1)[0]
    while choice == ' ' or choice == 0:
        choice = sample(sack[0:10], 1)[0]
    card_row.append(choice)
    sack[choice] = ' '

    for counter in range(1, 9):
        border_counter += 1
        choice = sample(sack[int('{0}{1}'.format(counter, '0')):int('{0}{1}'.format(border_counter, '0'))], 1)[0]
        while choice == ' ':
            choice = sample(sack[int('{0}{1}'.format(counter, '0')):int('{0}{1}'.format(border_counter, '0'))], 1)[0]
        card_row.append(choice)
        sack[choice] = ' '

    for clear_position in range(0,4):
        position_in_card_row = sample(card_row, 1)[0]
        while position_in_card_row == ' ':
            position_in_card_row = sample(card_row, 1)[0]
        card_row[card_row.index(position_in_card_row)] = '  '

    sorted_row = ' '
    for element in card_row:
        sorted_row += '{} '.format(str(element))
    return sorted_row


print(row_generator())
