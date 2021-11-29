from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
import pandas as pd
from pandas.core.frame import DataFrame


def sentiment_scores(t, neg, neu, pos, compound): 
    sid_obj = SentimentIntensityAnalyzer() 
    sentiment_dict = sid_obj.polarity_scores(t)
    print("Overall sentiment dictionary is : ", sentiment_dict) 
    neg.append(sentiment_dict["neg"])
    neu.append(sentiment_dict["neu"])
    pos.append(sentiment_dict["pos"])
    compound.append(sentiment_dict["compound"])
    
if __name__ == "__main__" : 
    video_df = pd.read_csv('youtubeCSVDataSet.csv')

    features = list(video_df.columns)
    
    title = video_df['video_title'],
    likes = video_df['like_count'], 
    dislikes = video_df['dislike_count'],
    views = video_df['view_count'],
    #comment_count = video_df['comment_count'], 
    ldr = video_df['like_dislike_ratio']

    d1 = pd.DataFrame(video_df)
    neg = []
    neu = []
    pos = []
    compound = []
    count =1
    for title_obj in title:
        for t in title_obj:
            print(count)
            count += 1
            sentiment_scores(t, neg, neu, pos, compound)
        
    d1["neg"] = neg
    d1["neu"] = neu
    d1["pos"] = pos
    d1["compound"] = compound

    d1.to_csv('youtubeCSVDataSet.csv', index=True)