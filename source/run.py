import sys

from wordle import *

def run_games():    
    word_file = '/Users/mortenheinesorensen/projects/wordle/resources/Scrabble2019filtered.txt'
    score_file= '/Users/mortenheinesorensen/projects/wordle/resources/scores.txt'
    min = 0
    max = 12971
    startword = "LARES";
    if len(sys.argv)==3:
        min = int(sys.argv[1])
        max = int(sys.argv[2])
    if len(sys.argv)==2:
        startword = sys.argv[1]
    play_all_games(26,5,min,max,word_file,score_file,startword)

run_games()