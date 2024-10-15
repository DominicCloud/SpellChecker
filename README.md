# Hindi-Spellchecker

## Steps to be followed:

1. Download the code 
1. Create a virtual env 
1. Activate the virtual env
1. Run requirements.txt file
pip install -r requirements.txt
1. run flask by entering 'python app.py' in the terminal

A simple python-based web application that takes in an input of text string (a single word, a sentence, or even a paragraph). 

It uses **Levenshtein Distance** matrix to calculate the edit distance between the current word and every word in the corpus dictionary.

The program also checks for use of non-hindi words or common words (more technically known as **stopwords** )

Color codes are as follows:
-
`rgb(255, 0, 0)` indicates correction of a _misspelled_ word

`rgb(26, 165, 252)` indicates detection of a _non-hindi_ word.

`rgb(169, 169, 169)` indicates detection of a _pre-defined stopword_.
