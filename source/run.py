import sys
from wordle import play_all_startwords
from files import get_score_file, get_word_file

def run_startwords():
    min_startword = 0 # LARES
    max_startword = 11 # LARES
    if len(sys.argv)==3:
        min_startword = int(sys.argv[1])
        max_startword  = int(sys.argv[2])
    play_all_startwords(26,5,get_word_file(),get_score_file(),min_startword,max_startword,True)

run_startwords()