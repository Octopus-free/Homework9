from CardAndHandful import CardGeneration
from CheckingCard import CheckingCard


test_card = CardGeneration().create_card()
print(test_card)

test_check = CheckingCard()

test_barrel = int(input('бочонок '))
what_value = test_check.strike_numbers_answer_yes(1, test_barrel, test_card)

print(what_value)
print(type(what_value))

