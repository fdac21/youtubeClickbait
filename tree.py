
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pandas.core.frame import DataFrame

#from sklearn import preprocessing
from sklearn import tree
import graphviz
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    
    # Loading in the data
    video_df = pd.read_csv('youtubeCSVDataSet.csv', skipinitialspace=True)
    features = list(video_df.columns)
    print(features)
    #video_id,video_title,click_bait,channel_Id,category_id,channelTitle,description,duration,view_count,like_count,view_like_ratio,dislike_count,view_dislike_ratio,like_dislike_ratio,favorite_count,comment_countcomments_enabled,view_comment_ratio,hidden,comments_disabled
    
    usable_df = DataFrame({
    'likes': video_df['likes'], 
    'dislikes': video_df['dislikes'],
    'views': video_df['views'],
    'comment_count': video_df['comment_count'], 
    'ldr': video_df['ldr']
    })
    
    
    X_train, X_test, y_train, y_test = train_test_split(usable_df.to_numpy(), video_df['clickbait'].to_numpy(), test_size=.2)
    
    decision_tree = tree.DecisionTreeClassifier(random_state=0, max_depth=3)
    decision_tree = decision_tree.fit(X_train, y_train)

    y_pred = decision_tree.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    tree.plot_tree(decision_tree, feature_names=features, class_names=features)


if __name__ == '__main__':
    main()