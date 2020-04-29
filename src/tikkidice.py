hands = {'Aces', 'Kings', 'Queens', 'Jacks', 'Tens', 'Nines', 'Full House', 'Five of a Kind', 'Straight Flush', 'Royal Flush'}

# State
player_combos = dict()  # dictionary of dictionaries: player => scores per combo

# setup the new game
while True:
    name = input('Enter name of next player (or return if finished): ')
    if not name:
        break
    player_combos[name] = {hand: False for (hand) in hands}

for turn in range(5):
    # loop through the players,showing current score then capturing new score
    for player, combos in player_combos.items():
        print('\n{}\'s turn {}'.format(player, turn+1))
        open_combos = [combo for (combo, score) in combos.items() if not score]
        print('{}: you still need to get {}. Good luck!'.format(
            player, ', '.join(open_combos)))
        # dice = []
        # for i in range(10):
        #     dice.append(input('{}, what did you roll for die {}? '.format(player, i+1)))
        # TODO - verify input with user, give chance to correct
        # TODO - recommend optimal combo for given dice
        entered = 0
        for combo in open_combos:
            score = input(
                '{}: what did you score for {} (press return for next combo)? '.format(player, combo))
            if score and not int(score):
                print('Please enter numeric score')
                continue  # TODO: FIXME retry this combo
            if not score:
                continue
            player_combos[player][combo] = int(score)
            entered = entered+1
            if entered == 2:
                break

    print('\nEnd of round {}. The scores are:'.format(turn+1))
    totals = {sum(combo.values()): player
              for (player, combo) in player_combos.items()}
    for score, player in sorted(totals.items(), reverse=True):
        formatted_combos = ['{}={}'.format(combo, score or ':(')
                            for (combo, score) in player_combos[player].items()]
        print('* {} scored {} *'.format(player, score))
        print(', '.join(formatted_combos))
print('{} wins!'.format(sorted(totals.items(), reverse=True)[0][1]))
