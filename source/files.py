# LOAD FROM FILES
import numpy
       
def get_word_file():
    return '/Users/mortenheinesorensen/projects/wordle/resources/Scrabble2019filtered.txt'

def get_score_file():
    return '/Users/mortenheinesorensen/projects/wordle/resources/scores.txt'


# Read all words into array combinations and build up map inv_combinations from word to index.
def all_words(colors,holes,combinations,inv_combinations, file):
    load_words(colors,holes,file,combinations,inv_combinations)

def load_words(colors,holes, file,combinations,inv_combinations):
    i = 0
    lines = []
    with open(file) as f:
        lines = f.readlines()
        f.close()
    for line in lines:
        line = line.strip().upper()
        combinations.append(line)
        inv_combinations.update({line: i}) 
        i +=1

# File lines have form e.g. 0;1;22000 meaning 0th word (guess AAHED) against 1st word (secret AALII) scores 22000 
# Resulting cache xa then has e.g. xa[0][1]=22000, i.e. xa = [[22222,22000,...],...]
def all_scores(colors,holes,scores,file):
    load_scores(colors,holes,file,scores)

def load_scores(colors,holes,infile,xa):
    with open(infile,"r") as f:
        ya = []
        xp = -1
        while True:
            line = f.readline()
            if not line:
                xa.append(numpy.array(ya))
                break
            c = line.strip().split(';')
            x = int(c[0])
            s = int(c[2])
            if (xp == -1 or xp == x):
                ya.append(s)
            else:
                xa.append(numpy.array(ya, dtype='i2'))
                ya=[]
                ya.append(s)
            xp = x
    return numpy.array(xa)

def load_decision_tree(infile,decision_tree):
    with open(infile,"r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            c = line.strip().split(' ')
            game = []
            for x in c:
                game.append(x)
            decision_tree.append(game)
    return

        

