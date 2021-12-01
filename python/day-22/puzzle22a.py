fin = open('input.txt')
deck1, deck2 = fin.read().split('\n\n')
deck1, deck2 = deck1.split('\n'), deck2.split('\n')
del deck1[0]
del deck2[0]
del deck2[-1]
deck1, deck2 = [int(x) for x in deck1], [int(x) for x in deck2]
deck1.reverse()
deck2.reverse()
while deck1 and deck2:
    card1, card2 = deck1.pop(), deck2.pop()
    if card1 > card2:
        deck1.insert(0, card1)
        deck1.insert(0, card2)
    elif card2 > card1:
        deck2.insert(0, card2)
        deck2.insert(0, card1)
    else:
        print('something went wrong')

print(deck1)
print(deck2)
if deck1:
    score = sum([x * (deck1.index(x) + 1) for x in deck1])
else:
    score = sum([x * (deck2.index(x) + 1) for x in deck2])
print(score)
