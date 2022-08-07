# wordle
An algorithm to guess all secrets in at most 7 attempts.
It is possible with manual tinkering to make it as most 6 attempts, but this is the direct approach.

0. Modify the file paths in files.py to match your setup.
1. Run precompute_scores.py to precalculate all scores.
2. Run run.py to run all games with start word e.g. LARES.
3. Run wordle.sh to run all games with 8 start word lists in parallel.

For more explanation of the algorithm see http://formalit.dk/wordle.pdf and http://formalit.dk/WordleDemo.pdf.