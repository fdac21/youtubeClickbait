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

    # Marking data as clickbait or not
    marks = []
    for i in range(len(like_dislike_ratios)):
        marks.append(randrange(0, 2))
    video_df['clickbait'] = marks


    video_df.to_csv('edited_data.csv')

if __name__ == '__main__':
    main()