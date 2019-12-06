from random import sample


# класс для генерации мешка с бочонками
class HandfulGeneration:

    def __init__(self):
        self.handful = []

    # функция для заполнения мешка бочонками со значениями от 0 до 91
    def create(self):
        for number_from_handful in range(0, 91):
            self.handful.append(number_from_handful)
        return self.handful


class CardGeneration:

    def __init__(self):
        self.card_row = []
        self.border_counter = 1
        self.sack = HandfulGeneration().create()
        self.string_row = ' '

    def create_row(self):

        for row_number in range(0, 3):

        # рандомно выбираем бочонок из мешка для первой клетки карточки (значения от 1 до 9)
        # значение заменяем в мешке на ' ', для того чтобы не было дублей в других рядах одной и той же карточки
        choice = sample(self.sack[0:10], 1)[0]
        while choice == ' ' or choice == 0:
            choice = sample(self.sack[0:10], 1)[0]
        self.card_row.append(choice)
        self.sack[choice] = ' '

        # рандомно заполняем остальные клетки на карточке (значения от 10 до 90)
        # значение заменяем в мешке на ' ', для того чтобы не было дублей в других рядах одной и той же карточки
        for counter in range(1, 9):
            self.border_counter += 1
            choice = sample(self.sack[int('{0}{1}'.format(counter, '0')):int('{0}{1}'.format(self.border_counter, '0'))], 1)[0]
            while choice == ' ':
                choice = sample(self.sack[int('{0}{1}'.format(counter, '0')):int('{0}{1}'.format(self.border_counter, '0'))], 1)[0]
            self.card_row.append(choice)
            self.sack[choice] = ' '

        # в каждой строке карточки рандомно зачищаем 4 клетки из 9
        for clear_position in range(0, 4):
            position_in_card_row = sample(self.card_row, 1)[0]
            while position_in_card_row == ' ':
                position_in_card_row = sample(self.card_row, 1)[0]
            self.card_row[self.card_row.index(position_in_card_row)] = '  '

        for element in self.card_row:
            self.string_row += '{} '.format(str(element))
        return self.string_row


my_card = CardGeneration()
handful = my_card.create_row()

print(handful)