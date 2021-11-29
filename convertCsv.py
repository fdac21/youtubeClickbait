import csv
import fileData
import re

def convertCsv(fd):
    try:
        with open('youtubeCSVDataSet.csv', mode='w', encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            header = ['video_id', 'video_title' , 'click_bait' , 'channel_Id' , 'category_id' , 'channelTitle' ,
                    'description', 'duration' , 'view_count' , 'like_count' , 'view_like_ratio', 'dislike_count' ,
                    'view_dislike_ratio', 'like_dislike_ratio', 'favorite_count', 'comment_count',
                    'view_comment_ratio', 'hidden', 'comments_disabled']
            writer.writerow(header)

            i = 0

            for k, val in fd.videos_dict.items():
                if i >= 80000:
                    break
                video_id = fd.videos_dict[k].videoId
                video_title = fd.videos_dict[k].title
                click_bait = 0
                channel_Id = fd.videos_dict[k].channelId
                category_id = fd.videos_dict[k].categoryId
                channel_title = fd.videos_dict[k].channelTitle

                description = fd.videos_dict[k].description
                description = description.replace('\n', ' ')
                #print(description)


                duration = fd.videos_dict[k].duration
                hidden = 0
                if fd.videos_dict[k].viewCount == 'None':
                    view_count = 0
                    hidden = 1
                else:
                    view_count = int(fd.videos_dict[k].viewCount)
                if fd.videos_dict[k].likeCount == 'None':
                    like_count = 0
                    hidden = 1
                else:
                    like_count = int(fd.videos_dict[k].likeCount)
                
                if like_count == 0:
                    view_like_ratio = 0
                else:
                    view_like_ratio = int(view_count) / int(like_count)

                if fd.videos_dict[k].dislikeCount == 'None':
                    dislike_count = 0
                    hidden = 1
                else:
                    dislike_count = int(fd.videos_dict[k].dislikeCount)
                if dislike_count == 0:
                    view_dislike_ratio = 0
                    like_dislike_ratio = 0
                else:
                    view_dislike_ratio = int(view_count) / int(dislike_count)
                    like_dislike_ratio = int(like_count) / int(dislike_count)
                favorite_count = fd.videos_dict[k].favoriteCount

                if fd.videos_dict[k].commentCount == 'None':
                    comment_count = 0
                    comments_disabled = 1
                else:
                    comment_count = int(fd.videos_dict[k].commentCount)
                    comments_disabled = 0

                if comment_count != 0:
                    view_comment_ratio = int(view_count) / int(comment_count)
                else: 
                    comment_count = 0

                data = [video_id, video_title, click_bait, channel_Id, category_id, channel_title,
                        description, duration, view_count, like_count, view_like_ratio, dislike_count,
                        view_dislike_ratio, like_dislike_ratio, favorite_count, comment_count,
                        view_comment_ratio, hidden, comments_disabled]

                writer.writerow(data)
                i = i + 1

    except IOError:
            print('Data file cant be opened')