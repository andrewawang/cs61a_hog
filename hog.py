"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

"""
Uncommented code is the final code. First commented block of code is the spring 1st try. Last block is fall final code. Goal is to make programs as efficent as possible.
"""

######################
# Phase 1: Simulator #
######################

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
#11 lines
"""
2nd time around code
    pig_out=False
    score=0
    pig_out_score=0
    for k in range(0,num_rolls):
        current_roll=dice()
        if current_roll==1:
            pig_out=True
            pig_out_score+=1
        else:
            score+=current_roll
    if pig_out==True:
        if pig_out_score>11-num_rolls:
            return 11-num_rolls
        else:
            return pig_out_score
    return score
16 lines
"""

"""
first time around code:
    num_rolls_left=num_rolls
    current_roll=0
    score=0
    one_count=0
    while num_rolls_left>0:
        current_roll=dice()
        if current_roll==1:
            one_count+=1
        else: score+=current_roll
        num_rolls_left-=1

    if one_count>0:
        return one_count
    else: return score
13 lines
"""

def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    return max(opponent_score%10,opponent_score//10)+1
#1 line
    # END PROBLEM 2

    """
1st time
    if opponent_score%10>opponent_score//10:
        return opponent_score%10+1
    else:
        return opponent_score//10+1
4 lines
    """


# Write your prime functions here!
def is_prime(number):
    if number==1:
        return False
    for k in range(2,number):
        if number%k==0:
            return False
    return True
#6lines

"""
2nd time
    k=2 #divisor counter
    if number==1:
        return False
    while k<number:
        if number%k==0:
            return False
        k+=1
    return True
#8 lines

"""

"""
1st time around

counter=2
    if number==1:
        return False
    if number==2:
        return True
    while counter<number:
        if number/counter==number//counter:
            return False
        else:
            counter+=1
    if counter==number:
        return True

12 lines
"""

def next_prime(prime):
    k=1 #progress bar
    while k>0:
        if is_prime(prime+k)==True:
            return prime+k
        k+=1

#5 lines
"""1st time

    counter=number
    while counter>0:
        counter+=1
        if is_prime(counter)==True:
            return counter
5 lines
"""
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
#4 lines plus other functions
    # END PROBLEM 2
"""
1st time
if num_rolls==0:
        score=free_bacon(opponent_score)
    else:
        score=roll_dice(num_rolls,dice)
    if is_prime(score)==True:
        score=next_prime(score)
    if 25-num_rolls>score:
        return score
    else:
        return 25-num_rolls
10 lines rip pigs fly rule
"""

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


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5

    while score0<goal and score1<goal:
        dice=select_dice(score0,score1)
        if player==0: #player0's turn
            num_rolls=strategy0(score0,score1)
            score0+=take_turn(num_rolls,score1,dice) #
            player=1
        elif player==1:#player1's turn
            num_rolls=strategy1(score1,score0)
            #dice=select_dice(score1,score0)
            score1+=take_turn(num_rolls,score0,dice)
            #if is_swap(score1,score0)==True:
            #    score1,score0=score0,score1
            player=0
        if is_swap(score0,score1)==True:
            score0,score1=score1,score0
#15 lines


       # END PROBLEM 5
    return score0, score1

"""
   def playerscore(player):
        if player==0:
            return score0
        return score1

    def playerstrat(player):
        if player==0:
            return strategy0
        return strategy1

    curr_score=0
    curr_opp_score=0

    while curr_score<goal and curr_opp_score<goal:
        curr_score=playerscore(player)
        curr_opp_score=playerscore(other(player))
        curr_strat=playerstrat(player)
        curr_opp_strat=playerstrat(other(player))

        num_rolls=curr_strat(curr_score,curr_opp_score)
        dice=select_dice(curr_score,curr_opp_score)

        curr_score+=

        player=other(player)
    cant for my life figure out how to use other(player) efficiently
"""

"""
    2nd try fail
    def strategy(player):
        if player==0:
            return strategy0
        return strategy1

    def score(player):
        if player==0:
            return score0
        return score1
"""

"""while score(player)<goal or score(other(player))<goal:
        def strategy(player):
            if player==0:
                return strategy0
            return strategy1

        def score(player):
            if player==0:
                return score0
            return score1

        num_rolls=strategy(player)(score(player),score(other(player)))
        dice=select_dice(score(player),score(other(player)))
        curr_score=take_turn(num_rolls,score(other(player)),dice)
        if is_swap(score(player),score(other(player)))==True:
            score(player),score(other(player))=score(other(player)),score(player)
       # score(player) , score(other(player)) = swap( score(player) , score( other(player) ) )
        player=other(player)
"""

"""
    1st try
    num_rolls=0
    def dice_swapper(Condition):
        if Condition==True:
            return False
        else:
            return True

    while score0<goal and score1<goal:
        if player==0:
            dice=select_dice(score0, score1, dice_swapped)
            num_rolls=strategy0(score0,score1)
            if num_rolls==-1:
                dice_swapped=dice_swapper(dice_swapped)
                score0+=1
                if score0*2==score1 or score1*2==score0:
                    hold0=score0
                    score0=score1
                    score1=hold0
            else:
                #if dice_swapped==False:
                score0+=take_turn(num_rolls,score1,dice)
                if score0*2==score1 or score1*2==score0:
                    hold0=score0
                    score0=score1
                    score1=hold0
                #else:
                    #score0+=take_turn(num_rolls,score1,four_sided)
        if player==1:
            dice=select_dice(score1, score0, dice_swapped)
            num_rolls=strategy1(score1,score0)
            if num_rolls==-1:
                dice_swapped=dice_swapper(dice_swapped)
                score1+=1
                if score0*2==score1 or score1*2==score0:
                    hold0=score0
                    score0=score1
                    score1=hold0
            else:
                #if dice_swapped==False:
                score1+=take_turn(num_rolls,score0,dice)
                if score0*2==score1 or score1*2==score0:
                    hold0=score0
                    score0=score1
                    score1=hold0
                #else:
                    #score1+=take_turn(num_rolls,score0,four_sided)

        player=other(player)
"""

#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert 0 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the
    strategy returns a valid input. Use `check_strategy_roll` to raise
    an error with a helpful message if the strategy returns an invalid
    output.

    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> check_strategy(fail_102_115)
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 6
    for k in range(0,goal):

        for z in range(0,goal):
            #num_rolls=strategy(k,z)
            check_strategy_roll(k,z,strategy(k,z))
        check_strategy_roll(k,z,strategy(k,z))
        #4 lines
    # END PROBLEM 6

"""
    score = 0 # score
    opponent_score = 0 # opponent score

    while score<goal:
        opponent_score=0
        while opponent_score<goal:
            num_rolls=strategy(score,opponent_score)
            check_strategy_roll(score,opponent_score,num_rolls)
            opponent_score+=1
        score+=1
1st time 9 lines
"""

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    """
    # BEGIN PROBLEM 7
    def iterator(*args):
        score_count=0
        for k in range(0,num_samples):
            score_count+=fn(*args)
        return score_count/num_samples
    return iterator
#6 lines
    # END PROBLEM 7

"""
def func(*args):
        counter=0
        value=0
        while counter<num_samples:
            value+=fn(*args)
            counter+=1
        return value/num_samples
    return func
#8 lines
"""


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN PROBLEM 8
    roll_score=make_averaged(roll_dice,num_samples)
    #max_rolls=0
    max_roll_score=0
    for k in range(1,11):
        if roll_score(k,dice)>max_roll_score:
            max_roll_score=roll_score(k,dice)
            max_rolls=k
    return max_rolls
#7 lines
    # END PROBLEM 8

"""
    turn_score_temp=0
    max_turn_score=0
    roll_amount=0
    for counter in range (1,11):
        turn_score_temp_func=make_averaged(roll_dice, num_samples)
        turn_score_temp=turn_score_temp_func(counter,dice)
        if turn_score_temp>max_turn_score:
            max_turn_score=turn_score_temp
            roll_amount=counter
    return roll_amount
10 lines
"""
def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""

    if False:
        z=0
        for k in range(0,500):
            z+=max_scoring_num_rolls(six_sided)
        print('Avg per turn roll for six sided', z/500)

    if False:
        z=0
        for k in range(0,500):
            z+=max_scoring_num_rolls(four_sided)
        print('Avg per turn roll for six sided', z/500)



    if False:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)
#####################################################################################
###############################################################
########################################################################
###################################################################
#1-10 checker
    if False:
        for k in range(1,11):
            print('always roll(',k,')', average_win_rate(always_roll(k)))

    if False:  # Change to True to test always_roll(5)
       print('always_roll(4) win rate:', average_win_rate(always_roll(4)))

    if False:  # Change to True to test always_roll(8)
        print('always_roll(6) win rate:', average_win_rate(always_roll(6)))


    if True:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))


    if False: #best margin checker BROKEN
        for k in range(0,15):
            z=0
            for c in range(0,1000):
                z+=average_win_rate(bacon_strategy(score, opponent_score, margin=k, num_rolls=6))
            print('bacon_strategy win rate for',k,':', z/1000)

##############################################
    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if False:  # Change to True to test is_swap_strat
        print('is_swap_strat win rate:', average_win_rate(is_swap_strat))

    if True:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=9, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 9
    if hog_prime(free_bacon(opponent_score))>=margin:
        return 0
    return num_rolls
    # END PROBLEM 9

    #3 lines
"""
bacon_score=free_bacon(opponent_score)
    if is_prime(bacon_score)==True:
        bacon_score=next_prime(bacon_score)
    if bacon_score>=margin:
        return 0
    else:
        return num_rolls
7 lines
"""
check_strategy(bacon_strategy)


def swap_strategy(score, opponent_score, margin=9, num_rolls=5):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 10
    if is_swap(score+free_bacon(opponent_score),opponent_score) or bacon_strategy(score,opponent_score,margin,num_rolls)==0:
        return 0
    return num_rolls  # Replace this statement
    # END PROBLEM 10
#3 lines
check_strategy(swap_strategy)

"""
bacon_roll=bacon_strategy(score,opponent_score, margin, num_rolls)
    bacon_score=free_bacon(opponent_score)
    if is_prime(bacon_score)==True:
        bacon_score=next_prime(bacon_score)
    if bacon_roll == 0:
        return 0
    elif (score+bacon_score)*2==opponent_score:
        return 0

    else:
        return num_rolls
10 lines
"""

def roll_dice_final_score(num_rolls,dice):
    return hog_prime(roll_dice(num_rolls,dice))

def bacon_strategy_check(score, opponent_score, margin=9, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 9
    if hog_prime(free_bacon(opponent_score))>=margin:
        return True, hog_prime(free_bacon(opponent_score))
    return False, 0

def is_swap_strat(score, opponent_score, margin=9, num_rolls=5):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 10
    if is_swap(score+free_bacon(opponent_score),opponent_score) or bacon_strategy(score,opponent_score,margin,num_rolls)==0:
        return 0
    return num_rolls

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    1st we find the default roll # that gives us the best results overall.
    Go to run experiment and set it to run 1-10.

    Notes: 1 is absolute crap. 2 is meh. 3 is decent. 4,5,6,7 best. 8,9,10 meh
    5,6 overall best for just one # roll. But barely over .5

    Per turn default roll #:
    my 2.0ghz laptop with python's lack of multicore or hyperthreading made this take forever
    six sided: 6.736
    four sided: 5.175

    6 overall best default

    next up is the two meta strats

    def bacon_strategy(score, opponent_score, margin=8, num_rolls=4)

    swap_strat

    best strat needs to have effective margin, already determined num_roll default

    time to check best margins for each strat
    bacon: 6 is lowest better than default
    9 best, 10 right behind it

    swap:8 lowest
    9 best

    tl;dr
    6 default, 9 margin
    .55 default, .6 margin strats. Need .65, combo should hit .65

    fak this isnt hitting >.6 consistiently. back to the drawing board

    we input two scores and we want the biggest scoring turn roll #

    what gives us points?

    free bacon: one more than their score, score between 1-10

    gotta apply hog_prime to everything except swap

    hog wild-want to trigger hog wild for yourself since its good;except you want to not give the other guy four sided dice


    trigger swine swap only if good

    take_turn(num_rolls, opponent_score, dice=six_sided):
    returns score for turn, before hog wild and swine swap

    .............2 days later still stuck

    four_sided change parameters works, gave us 2%

    ....
    didn't update for a few hours of work

    did a bunch of case specific testing, bless 5.0ghz OC to not waste too much time waiting

    isolating a few specific cases gets us the 65 win rate. next is maybe go for higher but i dont really care
"""
    # BEGIN PROBLEM 11
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
    #"""


#the rest here is just trash code from failed tests


    """
    #if (score+opponent_score)%7==0:
    #    return num_rolls

    #if hog_prime(free_bacon(opponent_score))>=margin:
    #    return 0

    free_bacon_work,bacon_turn_score=bacon_strategy_check(score, opponent_score, margin, num_rolls)

    if free_bacon_work==True:
        bacon_turn_score=turn_score


    #if opponent_score>50 and score<opponent_score/2:
    #    if is_swap_good(score+free_bacon(opponent_score),opponent_score) or bacon_strategy(score,opponent_score,margin,num_rolls)==0:
    #        return 0


    if is_swap_good(score+free_bacon(opponent_score),opponent_score):
        swap_turn_score=opponent_score*3/2-score
        swap_works=True

    if free_bacon_work or swap_works:
        return 0






    return num_rolls

    """

    """
    #roll 0
    #free bacon
    turn_score=hog_prime(free_bacon(opponent_score))
    if turn_score>top_turn_score:
        top_turn_score=turn_score
        best_roll_count=0
    #swap checker
    if is_swap_strat(score+turn_score,opponent_score):
        top_turn_score=opponent_score+turn_score
    """


    #print(take_turn(num_rolls, opponent_score, dice=six_sided))) #assume they didnt give us a 4 side
#num_roll sweep checker

    """
    for k in range(0,11):
        turn_score=take_turn(k, opponent_score, dice=six_sided)

        if (score+turn_score+opponent_score)%7==0:
            turn_score=0


        if turn_score>top_turn_score:
            best_roll_count=k
            top_turn_score=turn_score


    return best_roll_count
    """
    """
    if is_swap(score+free_bacon(opponent_score),opponent_score) or bacon_strategy(score,opponent_score,margin,num_rolls)==0:
        return 0

    elif hog_prime(free_bacon(opponent_score))>=margin:
        return 0



    return 6  # Replace this statement
    """
    return 6
    # END PROBLEM 11
check_strategy(final_strategy)


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
