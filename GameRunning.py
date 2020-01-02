from PlayersCondition import PlayersCondition
from CardAndHandful import  HandfulGame
from GameTurns import NextTurn
from CheckingCard import CheckingCard

# создаем экземплеяр класса PlayersCondition
# для запроса кол-ва игроков
players_count = PlayersCondition().asking_players()

# создаем листы, содержащие карточки для игры в лото
# для игроков людей и игроков компьютеров
human_players_list = PlayersCondition().create_cards_for_human(players_count[0])
computers_players_list = PlayersCondition().create_cards_for_computers(players_count[1])

# создаем экземпляр класса HandfulGame
# для генерации мешка с бочонками
barrels_for_game = HandfulGame().handful_using()

# создаем экземпляр класса NextTurn
# для генерации ходов игры лото
turn_for_game = NextTurn()

# создаем экземпляр класса CheckingCard
# для проверок карточек игроков
checks_for_game = CheckingCard()

for turn_number in range(1, 91):
    checks_for_game.check_human_players()