# This program guesses all secrets in Wordle in at most 7 guesses. By manual tinkering of the approach, the number can be reduced to 6.
# The program is based on a similar algorithm for master mind (MM). Some terminology is therefore adopted from MM. 
#
#   Holes = letter positions (5)
#   Colors = possible letters (26)
#   Peg (in guess) = Letter , represented by 0-25
#   Peg (in score) = Score for letter (grey, yellow, green, represented by 0-2)
#   Combination = Word (guess or secret), represent as either index number (i.e. 0-based linie number in file with words) or actual string of letters
#   Game = alternation of guess and score
#   Decision tree = cache, i.e. pair of a guess and a map from scores to new cache. 

import datetime

from files import all_words, all_scores
from games import empty_game, update_game
from decision_trees import empty_decision_tree, update_decision_tree, next_guess_from_tree

def output(s):
    return 
    #print(s)

# Score of guess against secret using cache
def score(guess,secret,colors,holes,inv_combinations,scores):
    i = inv_combinations[guess]
    j = inv_combinations[secret]
    s = scores[i][j]
    return int(s)

# Eliminate possible combinations by removing those for which the guess has different score than when compared to secret
def filter_combinations(possible_guesses, guess, guess_score,colors,holes,onlyQuantity,inv_combinations,scores):
    quantity=0
    new_possible_guesses = []
    for possible_guess in possible_guesses:
        score2 = score(guess,possible_guess,colors,holes,inv_combinations,scores)
        if (score2==guess_score) and not(guess==possible_guess):
            if (not(onlyQuantity)):
                new_possible_guesses.append(possible_guess)
            quantity +=1             
    return (new_possible_guesses,quantity)

# Find worst possible elimination for a given guess
def worst_elimination(guess, possible_guesses,colors,holes,min_possible_guesses,inv_combinations,scores):
    score_arr = {}
    for possible_guess in possible_guesses:
        score2 = score(guess,possible_guess,colors,holes,inv_combinations,scores)
        if (not (score2 in score_arr.keys())):
            score_arr[score2] = 0                
        score_arr[score2] += 1    
    max_possible_guess = 0
    for score2 in score_arr.keys():
        remaining_after_filter= score_arr[score2]
        if (remaining_after_filter > max_possible_guess):    
            max_possible_guess = remaining_after_filter
        if (max_possible_guess > min_possible_guesses):
            return max_possible_guess                
    return max_possible_guess

# Find guess that yields the mimimal maximal number of combinations, i.e. the best elimination of possible guesses
def best_guess_and_elimination(all_combinations,inv_combinations, possible_guesses,colors,holes,scores):
    best_guess = 0
    min_possible_guesses = 10000000
    possible_guess = False
    count = 0
    for combination in all_combinations:
        count += 1
        elim = worst_elimination(combination, possible_guesses,colors,holes, min_possible_guesses,inv_combinations,scores)
        if (elim < min_possible_guesses):
            min_possible_guesses = elim
            best_guess = combination
            possible_guess = (best_guess in possible_guesses)
        elif (elim == min_possible_guesses and not(possible_guess) and (combination in possible_guesses)):
            min_possible_guesses = elim
            best_guess = combination
            possible_guess = True            
            best_guess = combination
            possible_guess = (best_guess in possible_guesses)
    return (min_possible_guesses,best_guess,possible_guess)
    
# Play one round, i.e. make guess and get score
def play_round(guess_score,possible_guesses,guess,attempts,colors,holes,all_combinations,inv_combinations,scores, decision_tree, game):
    attempts += 1
    new_possible_guesses = filter_combinations(possible_guesses, guess, guess_score,colors,holes,False,inv_combinations,scores)[0]
    output("Remainning possible guesses "+str(len(new_possible_guesses)))
    guess = next_guess_from_tree(decision_tree,game)
    if (guess!=0):
        output("Making cached guess "+guess)    
    else:
        result = best_guess_and_elimination(all_combinations, inv_combinations, new_possible_guesses,colors,holes,scores) 
        remaining = result[0]
        guess = result[1]
        possible = result[2]
        output("Making "+("possible" if possible else "impossible")+" guess "+guess+" with maximum "+str(remaining)+" possible guess left")    
    return (new_possible_guesses,guess, attempts)

# Play one game
def play_game(all_combinations,inv_combinations,colors,holes,scores,decision_tree,start_word,secret):
    ct1 = datetime.datetime.now()
    possible_guesses = all_combinations
    attempts = 1
    done = False
    guess = start_word
    output("Secret "+secret)
    output("Making initial guess "+guess)
    
    guess_score = score(guess,secret,colors,holes,inv_combinations,scores)
    output("Score "+str(guess_score)) 
    
    game = empty_game()
    update_game(game, guess, guess_score)
    update_decision_tree(decision_tree,game)

    if guess_score==22222:
        done = True
    while (not(done)):        
        result = play_round(guess_score,possible_guesses,guess,attempts,colors,holes,all_combinations,inv_combinations,scores,decision_tree, game)
        new_possible_guesses = result[0]
        guess = result[1]
        attempts= result[2]
        guess_score = score(guess,secret,colors,holes,inv_combinations,scores)
        output("Score "+str(guess_score)) 
        if guess_score==22222: 
            done = True
        else:
            possible_guesses=new_possible_guesses
            update_game(game,guess, guess_score)
            update_decision_tree(decision_tree,game)
    output("Correct guess in "+str(attempts)+" attempts")
    ct2 = datetime.datetime.now()
    output(ct2-ct1)
    return attempts

# Play all games from some number to some number with given start word
def play_all_games(colors,holes,min_game,max_game,start_word,skipOnMin7,combinations,inv_combinations,scores):
    print("Playing game for start word "+start_word)
    decision_tree = empty_decision_tree(start_word) 
    maxatt = 0
    com = 0
    ct1 = datetime.datetime.now()
    print("Playing game for secrets "+str(min_game)+" to "+str(max_game)+" at "+str(datetime.datetime.now()))
    for secret in combinations:
        if (min_game <= com and com <= max_game):
            print("Playing Game for secret "+str(com)+" at "+str(datetime.datetime.now()))
            attempt = play_game(combinations,inv_combinations,colors,holes,scores,decision_tree,start_word,secret)
            print("Playing Game for secret "+str(com)+" completed at "+str(datetime.datetime.now()))
            if (attempt>maxatt):
                maxatt=attempt
            output("-----------------------------")
            if (com>max_game):
                return
            if (maxatt > 6 and skipOnMin7):
                print("Skipping remaining games")
                break
        com += 1
    ct2 = datetime.datetime.now()
    print("Playing game for secrets "+str(min_game)+" to "+str(max_game)+" completed at "+str(datetime.datetime.now()))
    print("Max attempts "+str(maxatt))
    print(ct2-ct1)

# Play all games for some range of start words 
def play_all_startwords(colors,holes,word_file,score_file,min_startword,max_startword,skipOnMin7):
    print("Playing games for start words from "+str(min_startword)+" to "+str(max_startword))+" at "+str(datetime.datetime.now())
    combinations = []
    inv_combinations = {}
    all_words(colors,holes,combinations, inv_combinations, word_file)
    scores = []
    all_scores(colors, holes, scores, score_file)

    com = 0
    combinations = []
    inv_combinations = {}
    all_words(colors,holes,combinations, inv_combinations, word_file)
    for start_word in combinations:
        if (min_startword <= com and com <= max_startword):
            play_all_games(colors,holes,0,len(combinations),start_word,skipOnMin7,combinations,inv_combinations,scores)
        com+=1
    print("Playing games for start words from "+str(min_startword)+" to "+str(max_startword))+" completed at "++str(datetime.datetime.now())

