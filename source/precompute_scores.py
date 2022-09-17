# PRECOMPUTE SCORES
from wordle import all_words, all_scores, best_guess_and_elimination
from files import get_score_file, get_word_file

def best_start_word(colors,holes):
    combinations = []
    inv_combinations = {}
    scores = []
    all_words(colors,holes,combinations,inv_combinations,get_word_file())
    all_scores(get_score_file(),scores,26,5)
    result = best_guess_and_elimination(combinations, inv_combinations, combinations,colors,holes,scores) 
    print(str(result[0]))
    print(result[1]) 
 
def score2(guess,secret,colors,holes):
    score = ["0"] * holes
    guess_accounted_for = []
    secret_accounted_for = []
    for i in range(holes):
        guess_accounted_for.append(False)
        secret_accounted_for.append(False)
    
    for position in range(holes):
        if (guess[position] == secret[position]):
            score[position] = "2"
            guess_accounted_for[position] = True
            secret_accounted_for[position] = True
    
    secret_pos = -1;
    for secret_peg in secret:
        secret_pos += 1
        guess_pos = -1
        for guess_peg in guess:
            guess_pos += 1
            if (guess_pos!=secret_pos and guess_peg==secret_peg and guess_accounted_for[guess_pos]==False and secret_accounted_for[secret_pos]==False):
                guess_accounted_for[guess_pos] = True
                secret_accounted_for[secret_pos] = True
                score[guess_pos] = "1"
    return ''.join(score)
    

def precompute_scores(outfile,word_file,colors,holes):
    all_combinationss = []
    inv_combinations = {}
    all_words(colors,holes, all_combinationss,inv_combinations,word_file)
    with open(outfile,"w+") as g:
        i = -1
        for x in all_combinationss:
            j = -1
            i += 1
            for y in all_combinationss:
                j += 1
                s = score2(x,y, colors, holes)            
                g.write(str(i)+";"+str(j)+";"+s+"\n") 

precompute_scores(get_score_file(),get_word_file(), 26,5)
