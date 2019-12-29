from card_for_game import CardGeneration, HandfulGeneration
from game_turn import NextTurn
from card_for_game import HandfulGame
from re import findall

from random import sample


def under_line(func):
    def inner():
        print('--'*13)
        result = func()
        print('--'*13)
        return result
    return inner


barrel_for_game = HandfulGame()

player_card_for_game = CardGeneration()
computer_card_for_game = CardGeneration()


player_card = player_card_for_game.create_card()
computer_card = computer_card_for_game.create_card()

for i in HandfulGeneration().create(): #range(1, 4):
    if len(findall(r'[\d]', player_card)) == 0:
        print('Вы победили')
        exit(0)

    if len(findall(r'[\d]', computer_card)) == 0:
        print('Компьютер победил')
        exit(0)

    print(NextTurn().turn(i))
    current_barrel = barrel_for_game.handful_using()
    print(f'Выпал бочонок {current_barrel}')

    print('Ваша карточка ')

    print('--' * 13)
    print(player_card)
    print('--' * 13)

    print('\nКарточка соперника')
    print('--' * 13)
    print(computer_card)
    print('--' * 13)
    strike_number = input('Зачеркнуть номер? ')

    if strike_number.lower() == 'да':
        if current_barrel < 10:
            if ' {} '.format(current_barrel) in player_card:
                player_card = player_card.replace(' {} '.format(current_barrel), ' - ')
            else:
                print('Вы проиграли, выпавшего бочонка нет на вашей карточке!')
                exit(0)

            if ' {} '.format(current_barrel) in computer_card:
                computer_card = computer_card.replace(' {} '.format(current_barrel), ' - ')
        else:
            if f' {current_barrel}' in player_card:
                player_card = player_card.replace(str(current_barrel), '--')
            else:
                print('Вы проиграли, выпавшего бочонка нет на вашей карточке!')
                exit(0)

            if f' {current_barrel}' in computer_card:
                computer_card = computer_card.replace(str(current_barrel), '--')
    else:
        if current_barrel < 10:
            if ' {} '.format(current_barrel) in player_card:
                print('Вы проиграли, необходимо было зачеркнуть число, выпавшее на бочонке!')
            if ' {} '.format(current_barrel) in computer_card:
                computer_card = computer_card.replace(' {} '.format(current_barrel), ' - ')
        else:
            if f' {current_barrel}' in player_card:
                print('Вы проиграли, необходимо было зачеркнуть число, выпавшее на бочонке!')
            if f' {current_barrel}' in computer_card:
                computer_card = computer_card.replace(str(current_barrel), '--')

    if len(findall(r'[\d]', player_card)) == 0:
        print('Вы победили')
        exit(0)

    if len(findall(r'[\d]', computer_card)) == 0:
        print('Компьютер победил')
        exit(0)




