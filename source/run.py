import sys
from decision_trees import empty_decision_tree
from wordle import play_all_startwords, play_game, best_guess_and_elimination, worst_elimination
from files import get_score_file, get_word_file, all_words, all_scores

def run_play_all_startwords():
    min_startword = 6096 # LARES
    max_startword = 6096 # LARES
    if len(sys.argv)==3:
        min_startword = int(sys.argv[1])
        max_startword  = int(sys.argv[2])
    play_all_startwords(26,5,get_word_file(),get_score_file(),min_startword,max_startword,True)


def run_play_game():
    start_word = 'LARES' # LARES
    secret = 'WANGS'
    combinations = []
    inv_combinations = {}
    all_words(26,5,combinations, inv_combinations, get_word_file())
    scores = []
    all_scores(26, 5, scores, get_score_file())
    decision_tree = empty_decision_tree(start_word) 
    play_game(combinations,inv_combinations,26,5,scores,decision_tree,start_word,secret)
        
    
def run_best_guess_and_elimination():
    combinations = []
    inv_combinations = {}
    all_words(26,5,combinations, inv_combinations, get_word_file())
    scores = []
    all_scores(26, 5, scores, get_score_file())
    best_guess_and_elimination(combinations,inv_combinations, combinations,26,5,scores)

def run_worst_elimination():
    combinations = []
    inv_combinations = {}
    all_words(26,5,combinations, inv_combinations, get_word_file())
    scores = []
    all_scores(26, 5, scores, get_score_file())
    worst_elimination('LARES',combinations,26,5,1000000,inv_combinations,scores)
    

#run_play_all_startwords()
#run_play_game()
#run_best_guess_and_elimination()
run_worst_elimination()
