import sys
from wordle import play_all_games
from files import get_score_file, get_word_file

def run_games():    
    min = 0
    max = 12971
    startword = "LARES";
    if len(sys.argv)==3:
        min = int(sys.argv[1])
        max = int(sys.argv[2])
    if len(sys.argv)==2:
        startword = sys.argv[1]
    play_all_games(26,5,min,max,get_word_file(),get_score_file(),startword)

run_games()