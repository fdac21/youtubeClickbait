import math

import pandas as pd
import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt

from pandas.core.frame import DataFrame

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def encode_titles(titles)-> list:
    t_dict = {}
    
    uid = 0
    for entry in titles:
        words = entry.split(' ')
        
        for word in words:
            uid += 1
            if word not in t_dict.keys():
                t_dict[word] = uid
        
    ret = []
    for entry in titles:
        words = entry.split(' ')
        tmp = ''
        for word in words:
            if word in t_dict.keys():
                tmp+=str(t_dict[word])
        ret.append(tmp)
    return ret

def tags_to_num(nums)-> int:
    ret = ''

    idk = nums.replace(' ', '')
    idk = idk.replace('[', '')
    idk = idk.replace(']', '')
    idk = idk.split(',')
    
    
    for x, entry in enumerate(idk):
        
        st = str(entry)
        tmst = ''
        #tmst += ('0' * (8 - (len(st))))
        ret += tmst+st
        if x == 5:
            break
    
    return ret

def main():
    
    # Loading in the data
    video_df = pd.read_csv('youtubeCSVDataSet.csv', skipinitialspace=True)
    features = list(video_df.columns)
    #print(features)

    video_df['video_title'] = encode_titles(video_df['video_title'])
 
    usable_df = DataFrame({
    'like_count': video_df['like_count'], 
    'dislike_count': video_df['dislike_count'],
    'view_count': video_df['view_count'],
    'comment_count': video_df['comment_count'], 
    'comments_disabled': video_df['comments_disabled'],
    #'ratings_disabled': video_df['ratings_disabled'], 
    'category_id': video_df['category_id'],
    #'tags': video_df['tags'],
    'video_title': video_df['video_title'],
    'view_like_ratio': video_df['view_like_ratio'],
    'view_dislike_ratio': video_df['view_dislike_ratio'],
    'view_comment_ratio': video_df['view_comment_ratio'],
    'like_dislike_ratio': video_df['like_dislike_ratio'],
    'neg': video_df['neg'],
    'neu': video_df['neu'],
    'pos': video_df['pos'],
    'compound': video_df['compound'],
    'hidden': video_df['hidden']
    })
    
    #print(video_df['click_bait'])

    for j in range(0, 1):
        X_train, X_test, y_train, y_test = train_test_split(usable_df.to_numpy(), video_df['click_bait'].to_numpy(), test_size=.2)
        
        model = MLPClassifier()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        print('Acc: {0}'.format(accuracy_score(y_test, y_pred)))

    '''
    fig, axes = plt.subplots(1,1)
    #axes = sns.pairplot(usable_df)
    #axes = sns.heatmap(usable_df) 
    plt.show()
    '''
    

if __name__ == '__main__':
    main()