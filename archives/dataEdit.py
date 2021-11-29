'''
    This is step 1, making the data usable for the algorithm and to graph.
    This is followed by running the clean_data.py which removes some samples that have
    errors in their data. The two files should be linked just have not yet.
'''

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from pandas.core.frame import DataFrame
from random import randrange

def main():
    
    # Loading in the data
    video_df = pd.read_csv('USvideos.csv', skipinitialspace=True)
    features = list(video_df.columns)
    
    # Flase and True -? 0, 1
    add_to_df = []
    for entry in video_df['comments_disabled']:
        if entry == 'False':
            add_to_df.append(0) 
        else:
            add_to_df.append(1)


    video_df['comments_disabled'] = add_to_df

    add_to_df = []
    for entry in video_df['ratings_disabled']:
        if entry == 'False':
            add_to_df.append(0) 
        else:
            add_to_df.append(1)

    video_df['ratings_disabled'] = add_to_df


    # Creating the like / dislike ratios
    likes = video_df['likes']
    dislikes = video_df['dislikes']

    like_dislike_ratios = []
    for x, y, in zip(likes, dislikes):
        if y == 0:
            like_dislike_ratios.append(x)
        else:
            like_dislike_ratios.append(x/y)

    video_df['ldr'] = like_dislike_ratios


    # Num spaces in title
    len_of_titles = []
    titles = video_df[features[2]]
    
    for title in titles:
        spaces = 0
        for letter in title:
            if letter == ' ':
                spaces+=1
        len_of_titles.append(spaces)

    video_df['spaces_in_titles']  = len_of_titles

    # Tag serialize
    tags_index = {}
    uid = -1
    for entry in video_df['tags']:
        words = entry.split('|')
        
        for word in words:
            uid += 1
            if word not in tags_index.keys():
                tags_index[word] = uid

    ser_tags = []
    for entry in video_df['tags']:
        stags = []

        words = entry.split('|')
        for word in words:
            if word in tags_index.keys():
                stags.append(tags_index[word])


        ser_tags.append(stags)

    video_df['tags'] = ser_tags
    
    '''
    features = list(video_df.columns)
    for entry in features:
        print(video_df[entry])
    '''
    
    # Marking data as clickbait or not
    marks = []
    for _ in range(len(like_dislike_ratios)):
        tmp = randrange(0, 2)
        if not tmp: 
            marks.append(0)
        else:
            marks.append(tmp)
    video_df['clickbait'] = marks

    for entry in marks:
        print(entry)



    video_df.to_csv('edited_data.csv')


if __name__ == '__main__':
    main()