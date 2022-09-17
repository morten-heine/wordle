# DECISION TREES AKA GUESS/SCORE CACHE

# Before any guess and score
def empty_decision_tree(start_word):
    return (start_word,{})

# Based on partial game [G0,S0,...Gn,Sn], update cache with S(n-1) -> Gn. 
def update_decision_tree(decision_tree,game):
    g, mp = decision_tree
    for i in range(len(game)-2):
        if i%2==1:
            if not game[i] in mp.keys():
                mp[game[i]]= empty_decision_tree(game[i+1])    
            g, mp = mp[game[i]]
    return


# Try to find next guess from partial game based on cache 
def next_guess_from_tree(decision_tree,game):
    g, mp = decision_tree
    for i in range(len(game)):
        if (i%2==1):
            if (game[i] in mp.keys()):
                g2, mp2 = mp[game[i]]
                if (i == len(game)-1):
                    return g2
                mp=mp2
    return 0;
