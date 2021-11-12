# https://developers.google.com/youtube/v3
# https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.htmlF
# pip install google-api-python-client      suggested vitrual client usefrom api import api_key

from api import api_key
from fileData import Video
from googleapiclient.discovery import build

#add videos to the videos_dict
def add_videos(response, fd):
    for pgToken in response:
        if pgToken not in fd.searchedTokens:
            fd.searchedTokens.add(pgToken)
            fd.new_tokens.add(pgToken)
        dictOfFive = response.get(pgToken)
        listOfFive = dictOfFive.get("items")
        for item in range(len(listOfFive)):
            video = listOfFive[item]
            id = video.get("id")
            if id not in fd.videos_dict:
                contentDetails = video.get("contentDetails")
                statistics = video.get("statistics")
                snippet = video.get("snippet")
                channelId = snippet.get("channelId")
                title = snippet.get("title")
                description = snippet.get("description")
                description = description + "\n-??end-of-description??-\n"
                channelTitle = snippet.get("channelTitle")
                categoryId = snippet.get("categoryId")
                duration = contentDetails.get("duration")
                viewCount = statistics.get("viewCount")
                likeCount = statistics.get("likeCount")
                dislikeCount = statistics.get("dislikeCount")
                favoriteCount = statistics.get("favoriteCount")
                commentCount = statistics.get("commentCount")
                v = Video(id, title, channelId, categoryId, channelTitle,
                            description, duration, viewCount, likeCount, 
                            dislikeCount, favoriteCount, commentCount)
                fd.videos_dict[id] = v
                fd.new_videos.add(id)

    return len(fd.new_videos)

#add a single video to the video dict
def add_video_single(response, fd):
    items = response.get("items")
    print(type(items))
    video = items[0]
    id = video.get("id")
    if id not in fd.videos_dict:
        contentDetails = video.get("contentDetails")
        statistics = video.get("statistics")
        snippet = video.get("snippet")
        channelId = snippet.get("channelId")
        title = snippet.get("title")
        description = snippet.get("description")
        description = description + "\n-??end-of-description??-\n"
        channelTitle = snippet.get("channelTitle")
        categoryId = snippet.get("categoryId")
        duration = contentDetails.get("duration")
        viewCount = statistics.get("viewCount")
        likeCount = statistics.get("likeCount")
        dislikeCount = statistics.get("dislikeCount")
        favoriteCount = statistics.get("favoriteCount")
        commentCount = statistics.get("commentCount")
        v = Video(id, title, channelId, categoryId, channelTitle,
                    description, duration, viewCount, likeCount, 
                    dislikeCount, favoriteCount, commentCount)
        fd.videos_dict[id] = v
        fd.new_videos.add(id)

        return len(fd.new_videos)
    else:
        return 0

#write the new videos and tokens to the file
def write_new_videos(f, fd):
    for token in fd.new_tokens:
        if token != "none":
            f.write("Searched on pageToken: " + token + '\n')
    for id in fd.new_videos:
        v = fd.videos_dict[id]
        v.write_video(f)
        

# limit of 10,000 request per day 
# test on small amounts first before getting full data set
def most_popular(n, token, f, fd):
    n -= 1
    num_new = 0
    response = {}

    # if a token is given
    if(token != 'none'):
        youtubeV3 = build('youtube', 'v3', developerKey=api_key)
        request = youtubeV3.videos().list(
            part="id,statistics,contentDetails,snippet",
            chart="mostPopular",
            pageToken=token
            
        )
        response[token] = request.execute()
    # if token is none
    elif(token == 'none'):
        youtubeV3 = build('youtube', 'v3', developerKey=api_key)
        request = youtubeV3.videos().list(
            part="id,statistics,contentDetails,snippet",
            chart="mostPopular",
        )
        response[token] = request.execute()

    #if a valid response
    #probably need some error checking here
    print("request number: {}".format(1))
    if(response):
        nextPageToken = response[token].get('nextPageToken')
        
        #check if need to n more make more requests 
        for i in range (n):
            print("request number: {}".format(i+2))
            request = youtubeV3.videos().list(
                part="id,statistics,contentDetails,snippet",
                chart="mostPopular",
                pageToken=nextPageToken
            )
            response[str(nextPageToken)] = request.execute()
            nextPageToken = response[str(nextPageToken)].get('nextPageToken')
        num_new = add_videos(response, fd)
        
        if num_new > 0:
            write_new_videos(f, fd)
        print("new videos added: " + str(num_new))
        print("next page token: " + str(nextPageToken))

#search for a single video id
def single_id(given_id, f, fd):
    num_new = 0
    youtubeV3 = build('youtube', 'v3', developerKey=api_key)
    request = youtubeV3.videos().list(
        part="id,statistics,contentDetails,snippet",
        id=str(given_id)
    )
    response = request.execute()
    pageInfo = response.get("pageInfo")
    if pageInfo.get("totalResults") > 0:
        num_new = add_video_single(response, fd)
    if num_new > 0:
            write_new_videos(f, fd)
    print("new videos added: " + str(num_new))