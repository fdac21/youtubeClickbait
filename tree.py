
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

    usable_df = DataFrame({
        'likes' : video_df['like_count'], 
        'dislikes': video_df['dislike_count'],
        'views' : video_df['view_count'],
        'comment_count' : video_df['comment_count'], 
        'ldr': video_df['like_dislike_ratio'],
        'view_like_ratio': video_df['view_like_ratio'],
        'view_dislike_ratio': video_df['view_dislike_ratio'],
        'favorite_count': video_df['favorite_count'],
        'view_comment_ratio': video_df['view_comment_ratio'],
        'comments_disabled': video_df['comments_disabled'],
    })
    
    
    X_train, X_test, y_train, y_test = train_test_split(usable_df.to_numpy(), video_df['click_bait'].to_numpy(), test_size=.2)
    
    decision_tree = tree.DecisionTreeClassifier(random_state=0, max_depth=4)
    decision_tree = decision_tree.fit(X_train, y_train)

    y_pred = decision_tree.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    tree.plot_tree(decision_tree, feature_names=features, class_names=features)


if __name__ == '__main__':
    main()