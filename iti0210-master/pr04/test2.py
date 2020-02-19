import random

ENEMY = 0
ME = 1

ROLL = 0
PASS = 1

aiscore = 0
dummyscore = 0


def pig_game(ai_func, dummy):
    rolled = 0
    turn = ME
    my_points = enemy_points = 0

    while my_points < 100 and enemy_points < 100:
        print("AI points", my_points,
              "DUMMY points", enemy_points,
              "holding", rolled)

        if turn == ME:
            decision1 = ai_func(turn, rolled, enemy_points, my_points)
            if decision1 == PASS:
                print("AI decides to pass.")
                rolled = 0
                turn = ENEMY
            else:
                dieroll = random.randint(1, 6)
                print("AI rolled...", dieroll)
                if dieroll == 1:
                    my_points -= rolled  # lose all points again
                    rolled = 0
                    turn = ENEMY
                else:
                    rolled += dieroll
                    my_points += dieroll

        else:
            decision = dummy(turn, rolled, enemy_points, my_points)
            if decision == PASS:
                print("DUMMY decides to pass.")
                rolled = 0
                turn = ME
            else:
                dieroll = random.randint(1, 6)
                print("DUMMY rolled...", dieroll)
                if dieroll == 1:
                    enemy_points -= rolled  # lose all points again
                    rolled = 0
                    turn = ME
                else:
                    rolled += dieroll
                    enemy_points += dieroll

    if my_points >= 100:
        global aiscore
        aiscore += 1
        print("AI won!")

    elif enemy_points >= 100:


        global dummyscore
        dummyscore += 1
        print("DUMMY won.")


def dummy_ai(turn, rolled, my_points, opp_points):
    if rolled < 21:
        return ROLL
    else:
        return PASS


def minimax_ai(turn, rolled, my_points, opp_points):
    # this is the top level of search
    # we search all possible moves
    # (PASS and ROLL in case of the Pig game)
    # and pick the one that returns the highest minimax estimate

    ai_play = exp_minimax(ENEMY, True, rolled, my_points, opp_points, 4)
    player_play = exp_minimax(ME, False, 0, my_points, opp_points, 4)

    # print("!!!!! " + str(ai_play) + " | " + str(player_play))
    if ai_play >= player_play:
        return ROLL

    return PASS


def exp_minimax(turn, chance, rolled, my_points, opp_points, depth):
    # update remaining depth as we go deeper in the search tree
    depth = depth - 1

    # case 1a: somebody won, stop searching
    # return a high value if AI wins, low if it loses.
    if my_points >= 100:
        return 1000000000000
    elif opp_points >= 100:
        return -1000000000000

    # case 1b: out of depth, stop searching
    # return game state eval (should be between win and loss)

    if depth == 0:
        return my_points - opp_points  # add value

    # case 2: AI's turn (and NOT a chance node):
    # return max value of possible moves (recursively)
    if turn == ENEMY and not chance:
        a1 = exp_minimax(ENEMY, True, rolled, my_points, opp_points, depth)
        a2 = exp_minimax(ME, False, 0, my_points, opp_points, depth)

        return max([a1, a2])

    # change player
    # case 3: player's turn:
    # return min value (assume optimal action from player)
    if turn == ME and not chance:
        a1 = exp_minimax(ENEMY, True, rolled, my_points, opp_points, depth)
        a2 = exp_minimax(ME, False, 0, my_points, opp_points, depth)

        return min([a1, a2])

    # case 4: chance node:
    # return average of all dice rolls

    if chance:
        aver = 0

        if ENEMY:

            aver += exp_minimax(ME, False, 0, my_points, opp_points - rolled, depth)
            for u in range(2, 7):
                aver += exp_minimax(ENEMY, False, rolled + u, my_points, opp_points + u, depth)
            return aver / 6

        if ME:

            aver += exp_minimax(ENEMY, False, 0, my_points - rolled, opp_points, depth)
            for y in range(2, 7):
                aver += exp_minimax(ME, False, rolled + y, my_points + y, opp_points, depth)
            return aver / 6


# play
for i in range(500):
    pig_game(minimax_ai, dummy_ai)
print()
print("~~~~~~~~~~~~~~ AI " + str(aiscore) + ' | DUMMY ' + str(dummyscore))
