import random
from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact
GOAL_SCORE = 100
"""
This is a minimal contest submission file. You may also submit the full
hog.py from Project 1 as your contest entry.

Only this file will be submitted. Make sure to include any helper functions
from `hog.py` that you'll need here! For example, if you have a function to
calculate Free Bacon points, you should make sure it's added to this file
as well.
"""

TEAM_NAME = 'no multithreading :(' # Change this line!

def is_swap_good(score0,score1):
    if score1==2*score0:
        return True
    return False
def is_prime(number):
    if number==1:
        return False
    for k in range(2,number):
        if number%k==0:
            return False
    return True
def next_prime(prime):
    k=1 #progress bar
    while k>0:
        if is_prime(prime+k)==True:
            return prime+k
        k+=1
    return score
def hog_prime(score):
    if is_prime(score):
        return next_prime(score)

def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    return max(opponent_score%10,opponent_score//10)+1
def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog Wild).
    """
    # BEGIN PROBLEM 3
    if (score+opponent_score) % 7==0:
        return four_sided
    return six_sided

def final_strategy(score, opponent_score):
    #return 5

#round 1 strat
    if score==0 and opponent_score==0:
        return 4
    margin=9
    num_rolls=6
    goal=100
    free_bacon_work=False
    swap_works=False
    #dice=four_sided

    bacon_turn_score=0
    swap_turn_score=0

    turn_score=0
    top_turn_score=0
    best_roll_count=0

    if (score + hog_prime(free_bacon(opponent_score))) >=goal and (score + hog_prime(free_bacon(opponent_score)))!=2*opponent_score:
        return 0


    dice=select_dice(score, opponent_score)
    if dice==four_sided:
        num_rolls=4
        margin=5 #5:.611866 good

    if opponent_score>90:
        return -1
#dont want to kill yourself
    if (score+hog_prime(free_bacon(opponent_score)))==2*opponent_score:
        return 5

#case specifics
    if 0<score<=10 and 0<opponent_score<=10:
        #return 6
        return num_rolls


    if 10<score<=20 and 10<opponent_score<=20:
        #return 6
        return 7



    #.612057
    if is_swap_good(hog_prime(free_bacon(opponent_score))+score,opponent_score):
        return 0

    if score>=86:
        return 4

    if opponent_score-score>20:
        return 8

    if abs(opponent_score-score)<10:
        return random.randint(0,10)


     #.621

    #if score>=50:
    #    return num_rolls



    #""".61186
    #margin=10
    bacon = free_bacon(opponent_score)
    bacon = hog_prime(bacon)
    if bacon >= margin or opponent_score / 2 == score + bacon:
        return 0
    #bacon strat is last case for getting optimal points
    return num_rolls


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return the
    number of 1's rolled (capped at 11 - NUM_ROLLS).
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** REPLACE THIS LINE ***"

    pig_out_count=0
    reg_score=0
    for k in range(0,num_rolls):
        curr_roll=dice()
        if curr_roll==1:
            pig_out_count+=1
        else:
            reg_score+=curr_roll
    if pig_out_count==0:
        return reg_score
    return min(pig_out_count,11-num_rolls)
def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    return max(opponent_score%10,opponent_score//10)+1
def is_prime(number):
    if number==1:
        return False
    for k in range(2,number):
        if number%k==0:
            return False
    return True
def next_prime(prime):
    k=1 #progress bar
    while k>0:
        if is_prime(prime+k)==True:
            return prime+k
        k+=1
def hog_prime(score):
    if is_prime(score):
        return next_prime(score)
    return score

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime rule.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    if num_rolls==0:
        return hog_prime(free_bacon(opponent_score))
    else:
        return hog_prime(roll_dice(num_rolls,dice))
def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog Wild).
    """
    # BEGIN PROBLEM 3
    if (score+opponent_score) % 7==0:
        return four_sided
    return six_sided
#3 lines, last year problem was different
    # END PROBLEM 3

def is_swap(score0, score1):
    """Returns whether one of the scores is double the other.
    """
    # BEGIN PROBLEM 4
    if score0==2*score1 or score1==2*score0:
        return True
    return False

def is_swap_good(score0,score1):
    if score1==2*score0:
        return True
    return False

def swap(score0,score1):
    if is_swap(score0,score1):
        return score1, score0
    return score0,score1
#3 lines, last year 3+4 was merged
    # END PROBLEM 4

def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player
