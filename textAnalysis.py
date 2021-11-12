import re
#from bs4 import BeautifulSoup

def cleanWord(w):
    #this needs some work bad
    word_cleaned = re.sub("-&\|:@<>\*;/=\?!\[\]\(\)", "", w)
    return re.sub('^[0-9\.]*', "", word_cleaned)

def titleAnalysis(fd):

    #need to get all the youtube titles and put them into one string
    titles = ''

    for k, v in fd.videos_dict.items():
        titles += fd.titles(k, fd)
        titles += ' '

    #split the titles into words
    words_reg_ex = re.split('\s+', titles)

    # remove periods, commas, etc stuck to the edges of words
    for i in range(len(words_reg_ex)):
        words_reg_ex[i] = cleanWord(words_reg_ex[i])

    for i in range(len(words_reg_ex)):
        print(words_reg_ex[i])
    
