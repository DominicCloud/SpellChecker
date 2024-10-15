def tokenize(sentence):
    return sentence.strip().split()

predefined_stopwords = {'है।', 'ही', 'से', 'लिए', 'कर', 'को', 'हैं', 
                        'के', 'हो', 'नहीं', 'ने', 'का', 'कि', 'कहा', 
                        'की', 'भी', 'और', 'एक', 'में', 'इस', 'है', 'पर'}

def stopword_removal(tokenized_words, stopwords_set=predefined_stopwords):
    filtered_words = []
    for word in tokenized_words:
        if word in stopwords_set:
            continue
        filtered_words.append(word)
    
    return filtered_words