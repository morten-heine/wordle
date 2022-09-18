# DECISION TREES AKA GUESS/SCORE CACHE

# After a score
def empty_decision_tree(remaining,guess):
    return (remaining,guess,{})

# Based on partial game [G0,S0,...Gn,Sn], update cache with S(n-1) -> Gn. 
def update_decision_tree(decision_tree,remaining,game):
    r, g, mp = decision_tree
    for i in range(len(game)-2):
        if i%2==1:
            if not game[i] in mp.keys():
                mp[game[i]]= empty_decision_tree(remaining,game[i+1])    
            r, g, mp = mp[game[i]]
    return


# Try to find next guess from partial game based on cache 
def next_guess_from_tree(decision_tree,game):
    cache = str(game[0])
    r, g, mp = decision_tree
    for i in range(len(game)):
        if (i%2==1):
            if (game[i] in mp.keys()):
                r2, g2, mp2 = mp[game[i]]
                cache += ','+str(game[i])+'->'+str(g2)+' '
                if (i == len(game)-1):
                    #print('Found cached guess '+g2+' for game '+str(game)+' using cache '+cache)
                    return (r2,g2)
                mp=mp2
    return ([],0);
