import random
from random import choice

coin = choice(["head", "tails"])
print(coin)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
