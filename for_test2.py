from card_for_game import print_card, HandfulGeneration
from game_turn import NextTurn
from card_for_game import  HandfulGame
from random import sample


turn = NextTurn().turn()
barrel = HandfulGame().handful_using()

print(f'Ход {turn}')
print(f'Выпал бочонок {barrel}')
print('Ваша карточка ')
print_card()
print('Карточка соперника')
print_card()


