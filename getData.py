import sys
from api import api_key
from googleapiclient.discovery import build

searchedTokens = set()
videos_dict = {}
new_videos = set()
new_tokens = set()

class Video:
    def __init__(self, videoId, title, channelId, categoryId,
                channelTitle, description, duration, viewCount,
                likeCount, dislikeCount, favoriteCount,
                commentCount):
        self.videoId = videoId
        self.title = title
        self.channelId = channelId
        self.categoryId = categoryId
        self.channelTitle = channelTitle
        self.description = description
        self.duration = duration
        self.viewCount = viewCount
        self.likeCount = likeCount
        self.dislikeCount = dislikeCount
        self.favoriteCount = favoriteCount
        self.commentCount = commentCount
    
    def print_video(self):
        print("id: " + self.videoId)
        print("title: " + self.title)
        print("channelId: " + self.channelId)
        print("categoryId: " + self.categoryId)
        print("channelTitle: " + self.channelTitle)
        print("description: " + self.description)
        print("duration: " + self.duration)
        #print("dimension: " + self.dimension)
        #print("definition: " + self.definition)
        #print("caption: " + self.caption)
        #print("licensedContent: " + self.licensedContent)
        #print("regionRestriction: " + self.regionRestriction)
        #print("contentRating: " + self.contentRating)
        #print("projection: " + self.projection)
        print("viewCount: " + self.viewCount)
        print("likeCount: " + self.likeCount)
        print("dislikeCount: " + self.dislikeCount)
        print("favoriteCount: " + self.favoriteCount)
        print("commentCount: " + self.commentCount)

    def write_video(self, f):
            f.write("id: "+ self.videoId + '\n')
            f.write("title: " + str(self.title) + '\n')
            f.write("channelId: " + str(self.channelId) + '\n')
            f.write("categoryId: " + str(self.categoryId) + '\n')
            f.write("channelTitle: " + str(self.channelTitle) + '\n')
            f.write("description: \n")
            f.write(self.description)
            f.write("duration: " + self.duration + '\n')
            f.write("viewCount: " + self.viewCount + '\n')
            f.write("likeCount: " + self.likeCount + '\n')
            f.write("dislikeCount: " + self.dislikeCount + '\n')
            f.write("favoriteCount: " + self.favoriteCount + '\n')
            f.write("commentCount: " + self.commentCount + '\n')
            f.write("\n")
            f.flush()



# https://developers.google.com/youtube/v3
# https://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.htmlF
# pip install google-api-python-client      suggested vitrual client use

def read_file_data(f):
    for line in f:
        line = line.strip()
        #if the line is not a newline
        if line != '\n':
            #get the id of the data and the value itself
            data = line.split(": ", 1)
            id = data[0]
            if len(data) == 2:
                val = data[1]
            else:
                val = ''
        #if val is not empty read the entry
        if val:
            #read the previously searched pageTokens
            if id == "Searched on pageToken":
                if val != "none":
                    searchedTokens.add(val)
            #read the video
            elif id == "id":
                videoId = val
                title = f.readline().strip().split(": ", 1)
                channelId = f.readline().strip().split(": ", 1)
                categoryId = f.readline().strip().split(": ", 1)
                channelTitle = f.readline().strip().split(": ", 1)
                descId = f.readline()
                if descId == "description: \n":
                    description = ""
                    l = ""
                    while l != "-??end-of-description??-\n":
                        l = f.readline()
                        description += l    
                duration = f.readline().strip().split(": ", 1)
                viewCount = f.readline().strip().split(": ", 1)
                likeCount = f.readline().strip().split(": ", 1)
                dislikeCount = f.readline().strip().split(": ", 1)
                favoriteCount = f.readline().strip().split(": ", 1)
                commentCount = f.readline().strip().split(": ", 1)

                v = Video(videoId, title[1], channelId[1], categoryId[1], channelTitle[1],
                        description[1], duration[1], viewCount[1], likeCount[1] ,dislikeCount[1],
                        favoriteCount[1], commentCount[1])
                #v.print_video()
        
                if videoId not in videos_dict:
                    videos_dict[videoId] = v

    #print(searchedTokens)
    #for k in videos_dict:
    #    print(k)
    #    v = videos_dict[k]
    #    v.print_video()

def add_videos(response):
    for pgToken in response:
        if pgToken not in searchedTokens:
            searchedTokens.add(pgToken)
            new_tokens.add(pgToken)
        dictOfFive = response.get(pgToken)
        listOfFive = dictOfFive.get("items")
        for item in range(len(listOfFive)):
            video = listOfFive[item]
            id = video.get("id")
            if id not in videos_dict:
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
                videos_dict[id] = v
                new_videos.add(id)
    return len(new_videos)

def write_new_videos(f):
    for token in new_tokens:
        if token != "none":
            f.write("Searched on pageToken: " + token + '\n')
    for id in new_videos:
        v = videos_dict[id]
        v.write_video(f)
        

# limit of 10,000 request per day 
# test on small amounts first before getting full data set
def most_popular(n, token, f):
    n -= 1
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
    if(response):
        nextPageToken = response[token].get('nextPageToken')
        
        #check if need to n more make more requests 
        for i in range (n):
            request = youtubeV3.videos().list(
                part="id,statistics,contentDetails,snippet",
                chart="mostPopular",
                pageToken=nextPageToken
            )
            response[str(nextPageToken)] = request.execute()
            nextPageToken = response[str(nextPageToken)].get('nextPageToken')  
        num_new = add_videos(response)
        if num_new > 0:
            write_new_videos(f)
        print("new videos added = " + str(num_new))
        print("next page token: " + str(nextPageToken))


def main():
    numOfArguments = len(sys.argv)
    arg = sys.argv
    
    if numOfArguments < 2:
        print("usage: getData.py [option] [num of loops] [pageToken]")

    if numOfArguments == 4:
        option = sys.argv[1]
        numOfLoops = int(sys.argv[2])
        pageToken = sys.argv[3]
        try:
            with open('youtubeVideos.txt', mode='r+', encoding="utf-8") as f:
                if (option == 'popular'):
                    if (numOfLoops > 0) and (numOfLoops <= 4000):
                        read_file_data(f)
                        most_popular(numOfLoops, pageToken, f)
                    else:
                        print("number of loops must be between 1 and 4000")
                elif (option == 'cat'):
                    print("not implemented yet")
                else:
                    print('option: ' + option + ' not available')
        except IOError:
            print('File cant be opened')
    else:
        print("usage: getData.py [option] [num of loops] [pageToken]")

if __name__ == "__main__":
    main()