import re
from typing import Dict
#from bs4 import BeautifulSoup

def cleanWord(w):
    # might want to find the pattern "..." and leave it in. Right now it's removing all instances of "."
    # I left "…" this is as its the same but probably used much less

    # this is a list in order of what the characters I'm removing from each word
    # if you add or remove a character please test after each change as this is really easy to
    # get messed up
    #   |    ,    \-    \(    \)    \"    \:   .    '    –   “   ”   ’   [   \]   &   +   •   —   ‘
    word_cleaned = re.sub("[|,\-\(\)\"\:.'–“”’[\]&\+/•—‘]", "", w)
    return re.sub('^[0-9\.]*', "", word_cleaned)

# the amount of emojis is crazy. Might need to find a way to detect them and put them in there own group
#def is_emoji(s)

def titleAnalysis(fd, words_dict):

    #use this if you want to test on a limited data set
    #t = 0
    #limit = 100

    #get titles from videos ad split them up into words
    for k, v in fd.videos_dict.items():
        #if t >= limit:
        #    break
        title = fd.videos_dict[k].title
        words_reg_ex = re.split('\s+', title)

        #clean up each word add add them to the dictonary
        #words_dict    keys=word in title     values=set of video ids with that word
        for i in range(len(words_reg_ex)):
            cw = cleanWord(words_reg_ex[i])
            #print("word: {}".format(cw))

            #if the word has '$' or '?' or '!' or '#' or '*word*' its added to its own set
            if cw:
                if cw[0] == '$':
                    words_dict.setdefault('$', set()).add(k)
                elif cw[len(cw)-1] == '?':
                    words_dict.setdefault('?', set()).add(k)
                elif cw[len(cw)-1] == '!':
                     words_dict.setdefault('!', set()).add(k)
                elif cw[0] == '#':
                    words_dict.setdefault('#', set()).add(k)
                elif cw[0] == '*' or cw[len(cw)-1] == '*':
                    words_dict.setdefault('*', set()).add(k)
                else:
                    words_dict.setdefault(cw, set()).add(k)
        #t = t + 1
        #print('\n')
    
#prints the entire titles dictonary
#used for testing. Its too big right now to do just this
def print_titles_dict(words_dict):
    for k, v in words_dict.items():
        print("{}".format(k))
        for i in v:
            print("  {}".format(i))
            if type(v) is dict:
                for x, z in v.items():
                    print("      {}".format(z))

#prints specific entry in the dictonary
#searched on key
def print_titles_option(words_dict, dict_key):
    v = words_dict[dict_key]
    print(dict_key)
    for i in v:
        print("   {}".format(i))
        if type(v) is dict:
            for x, z in v.items():
                print("    {}".format(x))
                print("      {}".format(z))