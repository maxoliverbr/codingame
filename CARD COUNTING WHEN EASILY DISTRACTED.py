import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

stream_of_consciousness = input()
bust_threshold = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
deck_value = { 
         "2": 2,
         "3": 3,
         "4": 4,
         "5": 5,
         "6": 6,
         "7": 7,
         "8": 8,
         "9": 9,
         "T": 10,
         "J": 10,
         "Q": 10,
         "K": 10,
         "A": 1}


deck = { "2": 4,
         "3": 4,
         "4": 4,
         "5": 4,
         "6": 4,
         "7": 4,
         "8": 4,
         "9": 4,
         "T": 4,
         "J": 4,
         "Q": 4,
         "K": 4,
         "A": 4}


series = stream_of_consciousness.split(".")
#print(series, file=sys.stderr, flush=True)
#print(bust_threshold, file=sys.stderr, flush=True)

for observation in series:
    valid_series = False
    for card in observation:
        if card not in "KQJTA23456789":
            valid_series = False
            break
        else:
            valid_series = True

    if valid_series:
        #print(observation, file=sys.stderr, flush=True)
        for card in observation:
            deck[card] -=1
        

final_deck = [(x, deck[x]) for x in deck if deck[x] != 0]

bust_count = 0

#for cards in final_deck:
#    card, card_quant = cards   
#    card_total += card_quant

card_total = sum([card_quant for card, card_quant in final_deck])

for cards in final_deck:
    card, card_quant = cards
    if deck_value[card]<bust_threshold:
        bust_count+=card_quant

#print(final_deck, file=sys.stderr, flush=True)
#print(card_total, file=sys.stderr, flush=True)
#print(bust_count, file=sys.stderr, flush=True)
print(f"{round(bust_count/card_total*100)}%")
