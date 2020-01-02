# создаем класс для проверки карточек игроков
from re import findall


class CheckingCard:

    # функция для проверки всех зачеркнутых числе на карточке игрока человека
    def check_human_players(self, human_players_cards):

        for human_card in human_players_cards:
            if len(findall(r'[\d]', human_card)) == 0:
                human_winner = human_players_cards.index(human_card) + 1
                print(f'Игрок {human_winner} победил!')
                exit(0)

    # функция для проверки всех зачеркнутых числе на карточке игрока компьютера
    def check_computer_players(self, computers_players_cards):

        for computer_card in computers_players_cards:
            if len(findall(r'[\d]', computer_card)) == 0:
                computer_winner = computers_players_cards.index(computer_card) + 1
                print(f'Компьютер {computer_winner} победил!')
                exit(0)

    # функция для проверки наличия на карточке выпавшего бочонка
    # если человек считает, что на карточке выпавший бочонок есть
    def strike_numbers_answer_yes(self, player_number, barrel_number, player_card):

        if barrel_number < 10:
            if ' {} '.format(barrel_number) in player_card:
                player_card = player_card.replace(' {} '.format(barrel_number), ' - ')
            else:
                print(f'Игрок {player_number} проиграл, выпавшего бочонка нет на вашей карточке!')
                exit(0)
        else:
            if f' {barrel_number}' in player_card:
                player_card = player_card.replace(str(barrel_number), '--')
            else:
                print(f'Игрок {player_number} проиграл, выпавшего бочонка нет на вашей карточке!')
                exit(0)
        return player_card

    # функция для проверки наличия на карточке выпавшего бочонка
    # если человек считает, что на карточке выпавшего бочонок нет
    def strike_numbers_answer_no(self, player_number, barrel_number, player_card):

        if barrel_number < 10:
            if ' {} '.format(barrel_number) in player_card:
                print(f'Игрок {player_number} проиграл, необходимо было зачеркнуть число, выпавшее на бочонке!')
                exit(0)
        else:
            if f' {barrel_number}' in player_card:
                print(f'Игрок {player_number} проиграл, необходимо было зачеркнуть число, выпавшее на бочонке!')
                exit(0)

    # функция для автоматического зачеркичания выпавшего бочонка на карточке игрока компьютера
    def strike_numbers_for_computers(self, barrel_number, computers_players_cards):

        cards_list = []

        if barrel_number < 10:
            for card in computers_players_cards:
                if ' {} '.format(barrel_number) in card:
                    card = card.replace(' {} '.format(barrel_number), ' - ')
                    cards_list.append(card)
                else:
                    cards_list.append(card)
        else:
            for card in computers_players_cards:
                if f' {barrel_number}' in card:
                    card = card.replace(str(barrel_number), '--')
                    cards_list.append(card)
                else:
                    cards_list.append(card)
        return cards_list
