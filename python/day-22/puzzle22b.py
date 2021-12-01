def play_game(deck1, deck2):
    round = 1
    prev_decks = {}
    while deck1 and deck2:
        if (tuple(deck1), tuple(deck2)) in prev_decks:
            return 'player1'
        else:
            prev_decks[(tuple(deck1), tuple(deck2))] = ''

        card1, card2 = deck1.pop(), deck2.pop()
        if len(deck1) >= card1 and len(deck2) >= card2:
            winner = play_game(deck1[-card1:], deck2[-card2:])
        else:
            if card1 > card2:
                winner = 'player1'
            elif card2 > card1:
                winner = 'player2'
            else:
                print('something went wrong')

        if winner == 'player1':
            deck1.insert(0, card1)
            deck1.insert(0, card2)
        elif winner == 'player2':
            deck2.insert(0, card2)
            deck2.insert(0, card1)

        round += 1

    if deck1:
        return 'player1'
    elif deck2:
        return 'player2'

fin = open('input.txt')
deck1, deck2 = fin.read().split('\n\n')
deck1, deck2 = deck1.split('\n'), deck2.split('\n')
del deck1[0]
del deck2[0]
del deck2[-1]
deck1, deck2 = [int(x) for x in deck1], [int(x) for x in deck2]
deck1.reverse()
deck2.reverse()

winner = play_game(deck1, deck2)
if winner == 'player1':
    score = sum([x * (deck1.index(x) + 1) for x in deck1])
elif winner == 'player2':
    score = sum([x * (deck2.index(x) + 1) for x in deck2])
else:
    print('something went wrong')
print(score)
