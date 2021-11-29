import csv

#all the file data is stored in this class
class FileData:
    def __init__(self):
        self.searchedTokens = set()         #tokens that have been searched on
        self.videos_dict = {}               #dictonary videos that are in data file
        self.new_videos = set()             #new videos found that can be added to the file
        self.new_tokens = set()             #new tokens that can be added to the file
        self.not_added = {}                 #videos that were not added (no longer exist or privacy)
        
    #print all the video ids in the videos dictonary
    def print_dict_ids(self):
        for k, v in self.videos_dict.items():
            print("id: {}".format(k))
        print("videos_dict size: {}".format(len(self.videos_dict)))

#stores all the info about a video
class Video:

    #constructor that creates video class - set up data
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
    
    #prints all values of a video
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
        print('\n')

    #writes a video to the data file
    def write_video(self, f):
            f.write("id: "+ self.videoId + '\n')
            f.write("title: " + str(self.title) + '\n')
            f.write("channelId: " + str(self.channelId) + '\n')
            f.write("categoryId: " + str(self.categoryId) + '\n')
            f.write("channelTitle: " + str(self.channelTitle) + '\n')
            f.write("description: \n")
            f.write(self.description)
            f.write("duration: " + str(self.duration) + '\n')
            f.write("viewCount: " + str(self.viewCount) + '\n')
            f.write("likeCount: " + str(self.likeCount) + '\n')
            f.write("dislikeCount: " + str(self.dislikeCount) + '\n')
            f.write("favoriteCount: " + str(self.favoriteCount) + '\n')
            f.write("commentCount: " + str(self.commentCount) + '\n')
            f.write("\n")
            f.flush()
            print("ADDED VIDEO")
            print("video title: {}\n".format(str(self.title)))


#reads entire data file
def read_file_data(f, fd):
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
                    fd.searchedTokens.add(val)
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
                    l = f.readline()
                    #read the description until this line is hit
                    #this is so it can be multiple lines
                    while l != "-??end-of-description??-\n":
                        description += l
                        l = f.readline()
                        
                #print(description)  
                duration = f.readline().strip().split(": ", 1)
                viewCount = f.readline().strip().split(": ", 1)
                likeCount = f.readline().strip().split(": ", 1)
                dislikeCount = f.readline().strip().split(": ", 1)
                favoriteCount = f.readline().strip().split(": ", 1)
                commentCount = f.readline().strip().split(": ", 1)

                #set all the information into a video 
                v = Video(videoId, title[1], channelId[1], categoryId[1], channelTitle[1],
                        description, duration[1], viewCount[1], likeCount[1] ,dislikeCount[1],
                        favoriteCount[1], commentCount[1])
                #v.print_video()
                
                #then put the video into the dictonary
                if videoId not in fd.videos_dict:
                    fd.videos_dict[videoId] = v

# Data from data set of Trending Youtube Videos
# https://mitchelljolly.com/
# https://www.kaggle.com/datasnaek/youtube-new?select=USvideos.csv
# this doen't have to be run again. All the vidoes in this database have already been added
def read_mj_file(f, mjfd):
    reader = csv.reader(f)

    headers = []
    headers = next(reader)
    for row in reader:
        videoId = str(row[0])
        title = str(row[2])
        channelId = 'NA'
        categoryId = str(row[4])
        channelTitle = str(row[3])
        description = str(row[15])
        duration = 'NA'
        viewCount = str(row[7])
        likeCount = str(row[8])
        dislikeCount = str(row[9])
        favoriteCount = 'NA'
        commentCount = str(row[10])

        v = Video(videoId, title, channelId, categoryId, channelTitle,
                        description, duration, viewCount, likeCount,
                        dislikeCount, favoriteCount, commentCount)

        if videoId not in mjfd.videos_dict:
            mjfd.videos_dict[videoId] = v