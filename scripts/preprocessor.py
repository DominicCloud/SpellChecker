import re

def tokenize(sentence):
    return sentence.strip().split()

predefined_stopwords = {'है।', 'ही', 'से', 'लिए', 'कर', 'को', 'हैं', 
                        'के', 'हो', 'नहीं', 'ने', 'का', 'कि', 'कहा', 
                        'की', 'भी', 'और', 'एक', 'में', 'इस', 'है', 'पर'}


def is__not_hindi(word):
    # Regular expression to match Hindi characters
    hindi_pattern = re.compile("[\u0900-\u097F]")
    
    return not bool(hindi_pattern.search(word))


def has_non_hindi_characters(text):
    # Regular expression pattern to match non-Hindi characters
    non_hindi_pattern = re.compile("[^\u0900-\u097F\s]")  # Excludes Hindi characters and whitespace
    return bool(non_hindi_pattern.search(text))

def stopword_removal(tokenized_words, stopwords_set=predefined_stopwords):
    filtered_words = []
    for word in tokenized_words:
        if word in stopwords_set:
            continue
        filtered_words.append(word)
    
    return filtered_words

def is_stopword(word, stopwords_set=predefined_stopwords):
    return False if word not in stopwords_set else True