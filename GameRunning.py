from PlayersCondition import PlayersCondition
from CardAndHandful import HandfulGame
from GameTurns import NextTurn
from CheckingCard import CheckingCard
from PrintingCard import PrintingCard

# создаем экземплеяр класса PlayersCondition
# для запроса кол-ва игроков
players_count = PlayersCondition().asking_players()

# создаем листы, содержащие карточки для игры в лото
# для игроков людей и игроков компьютеров
human_players_cards = PlayersCondition().create_cards_for_human(players_count[0])
computers_players_cards = PlayersCondition().create_cards_for_computers(players_count[1])

# создаем экземпляр класса HandfulGame
# для генерации мешка с бочонками
barrels_for_game = HandfulGame()

# создаем экземпляр класса NextTurn
# для генерации ходов игры лото
turn_for_game = NextTurn()

# создаем экземпляр класса PrintingCard
# для отрисовки карточек игроков в терминале
print_for_game = PrintingCard()

# создаем экземпляр класса CheckingCard
# для проверок карточек игроков
checks_for_game = CheckingCard()

# создаем цикл для генерации ходов игры
for turn_number in range(1, 91):

    # объявляем номер текущего хода
    print(turn_for_game.turn_step(turn_number))

    # объявляем номер бочонка, выпавшего в текущем ходу
    current_barrel = barrels_for_game.handful_using()
    print(f'Выпал бочонок {current_barrel}')

    # отрисовываем в терминале карточки игроков людей
    # запрашиваем выбор игрока о зачеркивании выпавшего бочонка на карточке
    for human_card in human_players_cards:
        player_number = human_players_cards.index(human_card) + 1
        print_for_game.print_human_cards(player_number, human_card)
        strike_choice = input('Зачеркнуть номер? ')
        if strike_choice.lower() == 'да':
            card_after_check = checks_for_game.strike_numbers_answer_yes(player_number, current_barrel, human_card)
            human_players_cards[human_players_cards.index(human_card)] = card_after_check
        else:
            checks_for_game.strike_numbers_answer_no(player_number, current_barrel, human_card)

    # отрисовываем в терминале карточки игроков компьютеров и автоматически зачеркиваем выпавший бочонок
    print_for_game.print_computers_cards(computers_players_cards)
    computers_players_cards = checks_for_game.strike_numbers_for_computers(current_barrel, computers_players_cards)

    # в конце хода проверяем карточки игроков на предмет всех зачеркнутых чисел (победы)
    checks_for_game.check_human_players(human_players_cards)
    checks_for_game.check_computer_players(computers_players_cards)