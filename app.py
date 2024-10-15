# -*- coding: utf-8 -*-
import sys 
import os
from scripts.spell_check import *
from scripts.preprocessor import tokenize, stopword_removal
from flask import Flask,render_template, request, session

app = Flask(__name__)
 
c = []

def hindi(t):
    corpus=loadCorpus()
    words = t.strip().split()
    corrected=[]
    for word in words:
        if word not in corpus :
            corrected_word = getCorrectWord(word, corpus)
            corrected.append(f'<span class="corrected">{corrected_word}</span>')  # Mark corrected word
        else:
            corrected.append(word)    
    result=' '.join(corrected)
    return result

# def hindi(sentence):
#     corpus=loadCorpus()
#     tokenized_words = tokenize(sentence)
#     words = stopword_removal(tokenized_words)
#     corrected=[]
#     for word in words:
#         if word not in corpus :
#             corrected_word = getCorrectWord(word, corpus)
#             corrected.append(f'<span class="corrected">{corrected_word}</span>')  # Mark corrected word
#         else:
#             corrected.append(word)    
#     result=' '.join(corrected)
#     print(result)
#     return result

@app.route('/', methods=['GET'])
def index():
	return render_template('landing.html')

@app.route('/output', methods=['GET','POST'])
def process_input():
        
    if request.method == 'POST':
        t=request.form['input_text']
        res=hindi(t) 
    
        return render_template("landing.html",prediction =res, user_input=t)

# Main Function
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
