import math

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from pandas.core.frame import DataFrame

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

def main():
    
    # Loading in the data
    video_df = pd.read_csv('finalData.csv', skipinitialspace=True)
    features = list(video_df.columns)
    print(features)

    usable_df = DataFrame({
    'likes': video_df['likes'], 
    'dislikes': video_df['dislikes'],
    'views': video_df['views'],
    'comment_count': video_df['comment_count'], 
    'comments_disabled': video_df['comments_disabled'],
    'ratings_disabled': video_df['ratings_disabled'], 
    'category_id': video_df['category_id'],
    'ldr': video_df['ldr']
    })
    
    
    X_train, X_test, y_train, y_test = train_test_split(usable_df.to_numpy(), video_df['clickbait'].to_numpy(), test_size=.2)
    
    model = MLPClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    
    fig, axes = plt.subplots(1,1)
    #axes = sns.pairplot(usable_df)
    #axes = sns.heatmap(usable_df) 
    plt.show()
    
    

if __name__ == '__main__':
    main()